# main.py - A comprehensive Python starter script for GitHub's Linguist
# Created by Abie Haryatmo, enhanced by Gemini

class Project:
    """A simple class to represent our project."""
    def __init__(self, name):
        self.name = name
        self.version = "1.0.0"

    def display_info(self):
        """Prints project information."""
        print(f"Project Name: {self.name}")
        print(f"Version: {self.version}")

def main():
    """Main function to demonstrate various Python features."""
    my_project = Project("GitHub Auto-Repo Project")
    my_project.display_info()

    print("\nThis script is now comprehensive enough for GitHub's language detection.")
    
    # Example of a list and a loop
    features = ["Classes", "Functions", "Loops", "F-strings"]
    print("Features demonstrated:")
    for feature in features:
        print(f"  - {feature}")

if __name__ == "__main__":
    main()
