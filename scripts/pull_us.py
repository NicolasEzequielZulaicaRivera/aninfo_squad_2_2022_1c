import requests
import json
import os
import textwrap
import filecmp
import shutil
from datetime import datetime
import os

# from dotenv import load_dotenv

# If the repo requires authentication:
# Generate a personal access token from https://github.com/settings/tokens and add it to .env folder
# with key AUTH_TOKEN
# load_dotenv()

REPO_OWNER = "NicolasEzequielZulaicaRivera"
REPO_NAME = "aninfo_tribu_1_2022_1c"
ISSUES_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
FEATURES_FOLDER = "tests/features"
FEATURES_BACKUPS_FOLDER = f"{FEATURES_FOLDER}/backups"
MAX_LINE_LENGTH = 80


class NotAUserStory(Exception):
    pass


class NotOurModule(Exception):
    pass


class IssuesJsonList:
    def __init__(self, issues_url):
        response = requests.get(issues_url)
        self.issues_json = json.loads(response.text)

    def get(self):
        return self.issues_json


class FileWriter:
    @staticmethod
    def write_feature(user_story):
        feature_name = user_story.feature_name()
        feature_file_name = FileWriter.make_feature_folder_name(feature_name)

        if not os.path.exists(feature_file_name):
            with open(os.open(feature_file_name, os.O_CREAT | os.O_RDWR), "w") as f:
                f.write(user_story.gherkin_feature())
                f.write(user_story.gherkin_us_as_comment())
        else:
            with open(feature_file_name, "r") as f:
                lines = f.readlines()
            with open(feature_file_name, "w") as f:
                f.write(user_story.gherkin_feature())
                f.write(user_story.gherkin_us_as_comment())
                start_of_scenarios_line_number = Parser.end_of_us_description_comment(
                    lines
                )
                f.writelines(lines[start_of_scenarios_line_number:])

    @staticmethod
    def make_feature_folder_name(feature_name):
        return f"{FEATURES_FOLDER}/{feature_name}.feature"

    @staticmethod
    def make_features_backup():
        if not any(file.endswith(".feature") for file in os.listdir(FEATURES_FOLDER)):
            return

        now = datetime.now()
        folder_name = now.strftime("%Y-%m-%d-%H-%M-%S")
        os.makedirs(f"{FEATURES_BACKUPS_FOLDER}/{folder_name}")

        features_files = [
            f for f in os.listdir(FEATURES_FOLDER) if f.endswith(".feature")
        ]
        for feature_file in features_files:
            with open(f"{FEATURES_FOLDER}/{feature_file}", "r") as f:
                lines = f.readlines()
            with open(
                f"{FEATURES_BACKUPS_FOLDER}/" + folder_name + "/" + feature_file, "w"
            ) as f:
                f.writelines(lines)

        return folder_name

    @staticmethod
    def remove_files_without_changes(backup_folder):
        diff_files = filecmp.dircmp(
            FEATURES_BACKUPS_FOLDER + "/" + backup_folder, FEATURES_FOLDER
        ).diff_files
        if not diff_files:
            shutil.rmtree(FEATURES_BACKUPS_FOLDER + "/" + backup_folder)
        else:
            files_to_remove = [
                f
                for f in os.listdir(f"{FEATURES_BACKUPS_FOLDER}/{backup_folder}")
                if f not in diff_files
            ]
            for file in files_to_remove:
                os.remove(f"{FEATURES_BACKUPS_FOLDER}/{backup_folder}/{file}")

    @staticmethod
    def create_folder_if_not_exists(folder_name):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)


class Parser:
    @staticmethod
    def end_of_us_description_comment(lines):
        triple_quote_counter = 0
        for i, line in enumerate(lines):
            if '"""' in line:
                triple_quote_counter += 1
            if triple_quote_counter == 2:
                return i + 1
        return len(lines)


class UserStory:
    def __init__(self, issue_json):
        if not self._check_exist_label_us(issue_json):
            raise NotAUserStory

        if not self._check_exist_label_projects(issue_json):
            raise NotOurModule

        self.title = issue_json["title"]
        self.body = issue_json["body"]

    @staticmethod
    def _check_exist_label_projects(issue_json):
        labels = issue_json["labels"]
        for label in labels:
            if label["name"] == "Proyectos":
                return True
        return False

    @staticmethod
    def _check_exist_label_us(issue_json):
        labels = issue_json["labels"]
        for label in labels:
            if label["name"] == "US":
                return True
        return False

    def feature_name(self):
        self.title = self.title.lower()
        replacement = {
            "á": "a",
            "é": "e",
            "í": "i",
            "ó": "o",
            "ú": "u",
        }
        for k, v in replacement.items():
            self.title = self.title.replace(k, v)
        return self.title.replace(" ", "_")

    def gherkin_feature(self):
        return "Feature: " + self.title + "\n"

    def gherkin_us_as_comment(self):
        lines = []
        body_simplified = self.body.replace("**", "").replace("[ ] ", "")

        for line in body_simplified.split("\r\n"):
            line = textwrap.wrap(
                line,
                width=MAX_LINE_LENGTH,
                replace_whitespace=False,
                break_long_words=False,
                initial_indent="\t",
                subsequent_indent="\t",
            )

            lines_with_newline = "\n".join(line)
            lines.append(lines_with_newline)

        lines = "\n".join(lines)

        return '\t"""\n' + lines + '\n\t"""\n'


def main():
    FileWriter.create_folder_if_not_exists(FEATURES_FOLDER)
    FileWriter.create_folder_if_not_exists(FEATURES_BACKUPS_FOLDER)

    backup_folder = FileWriter.make_features_backup()

    issues_json_list = IssuesJsonList(ISSUES_URL).get()

    user_stories = []
    for issue_json in issues_json_list:
        try:
            user_story = UserStory(issue_json)
        except (NotAUserStory, NotOurModule):
            continue

        user_stories.append(user_story)

    for user_story in user_stories:
        FileWriter.write_feature(user_story)

    if backup_folder:
        FileWriter.remove_files_without_changes(backup_folder)


if __name__ == "__main__":
    main()
