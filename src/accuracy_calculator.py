import pandas as pd
import os

def calculate_accuracy(folder_path):
    correct_predictions = 0
    total_predictions = 0

    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

    for file in csv_files:
        df = pd.read_csv(os.path.join(folder_path, file))

        # 파일이 정답이 0인 상황인지 1인 상황인지 확인
        if "correct0" in file:
            correct_label = 0
        elif "correct1" in file:
            correct_label = 1
        else:
            continue

        # 정답과 예측값 비교
        correct_predictions += (df['ppg prediction'] == correct_label).sum()
        total_predictions += len(df)

    # 전체 정확도 계산
    accuracy = correct_predictions / total_predictions if total_predictions > 0 else 0
    return accuracy
