import os
from src.accuracy_calculator import calculate_accuracy


def main():
    folder_path = 'data'

    accuracy = calculate_accuracy(folder_path)

    print(f'Overall accuracy: {accuracy:.2%}')

    results_folder = 'results'
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    result_file = os.path.join(results_folder, 'accuracy_report.txt')
    with open(result_file, 'w') as f:
        f.write(f'Overall accuracy: {accuracy:.2%}\n')

    print(f'Accuracy report saved to {result_file}')


if __name__ == "__main__":
    main()
