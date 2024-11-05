import whisper
import subprocess
import os
import argparse

# ffmpeg -i ~/Videos/test.mp4 -ss 00:00:43 -to 00:01:00 -c copy output.mp4

model = whisper.load_model("large")


def main():
    parser = argparse.ArgumentParser(description="Process a file")
    parser.add_argument(
        "-i", "--input", type=str, required=True, help="Path to the input file"
    )
    args = parser.parse_args()

    input_file_path = args.input

    if os.path.isfile(input_file_path):
        process_file(input_file_path)
    else:
        process_files(input_file_path)


def process_files(dir: str):
    for file in os.listdir(dir):
        if file.endswith(".mp4"):
            process_file(os.path.join(dir, file))


def process_file(file_path: str):
    result = model.transcribe(
        file_path,
        word_timestamps=True,
        language="en",
    )

    marks = extract_start_stop_marks(result["segments"])

    base_path = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    out_path = os.path.join(base_path, f"{file_name}.out.mp4")

    cut_video(
        file_path,
        out_path,
        marks["start"],
        marks["stop"],
    )


def remove_non_alpha_lc(text):
    return "".join(char for char in text if char.isalpha())


def extract_start_stop_marks(segments: list) -> dict[str, int]:
    marks = {"start": 0, "stop": 0}
    for _, seg in enumerate(segments, start=1):
        text = remove_non_alpha_lc(seg["text"].strip().lower())
        marks[text] = seg["start"]
    return marks


def cut_video(input_file, output_file, start_time, end_time):
    subprocess.call(
        f'ffmpeg -i "{input_file}" -ss {start_time} -to {end_time} "{output_file}"',
        shell=True,
    )


if __name__ == "__main__":
    main()
