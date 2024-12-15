from experiment_comparison import ExperimentComparison


def main():
    # Define the experiment folders to compare
    experiment_folders = {"test": "data/bf91a4b2f8cf1a99ba21894297f05600", "exp2": "data/a6514a317834b0b96f7f5e536ff2fd25"}

    # Initialize the Compare class with the experiment folders
    compare = ExperimentComparison(experiment_folders)
    compare.execute_comparisons()

if __name__ == "__main__":
    main()

# TODO: Instead of putting legend in each graph, extract it once and save it to a new png