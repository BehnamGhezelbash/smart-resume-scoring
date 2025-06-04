

from parser import parse_all_resumes
from matcher import calculate_similarity_scores


def load_job_description(path):
    """
    Loads job description text from a file.
    """
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


def display_results(results):
    """
    Displays ranked resume results.
    """
    print("\n Resume Match Scores:")
    print("-" * 40)
    for i, (filename, score) in enumerate(results, 1):
        print(f"{i}. {filename:<25} Score: {score}")


if __name__ == "__main__":
    job_desc_path = "job_description.txt"
    resume_folder = "resumes"

    job_description = load_job_description(job_desc_path)
    resumes = parse_all_resumes(resume_folder)
    results = calculate_similarity_scores(job_description, resumes)

    display_results(results)
