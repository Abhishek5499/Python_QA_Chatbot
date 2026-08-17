# AI Resume Screening System

An AI-powered resume screening system that analyzes resumes and compares them with a given job description to identify the most relevant candidates.

The system extracts text from resumes, identifies relevant skills and requirements, calculates a matching score, and ranks candidates based on their relevance to the job description.

## Project Overview

Recruiters often receive a large number of resumes for a single job opening. Manually reviewing every resume can be time-consuming, repetitive, and prone to human error.

This project provides an automated approach to the initial resume screening process by comparing candidate resumes with a job description and generating a relevance score.

The system is designed as a **decision-support tool** for recruiters. It does not replace human decision-making.

## Objectives

- Accept a job description.
- Accept multiple resumes.
- Extract text from resumes.
- Identify relevant skills and requirements.
- Compare resumes with the job description.
- Calculate a matching score.
- Rank candidates based on relevance.
- Reduce the time required for initial resume screening.

## Key Features

- 📄 Resume text extraction
- 📝 Job description processing
- 🔍 Skill and keyword matching
- 📊 Resume-job matching score
- 🏆 Candidate ranking
- 💻 Interactive Streamlit interface
- 📁 Support for multiple resumes
- ⚡ Faster initial candidate screening

## System Workflow

```text
Job Description
       +
Multiple Resumes
       ↓
Resume Text Extraction
       ↓
Text Preprocessing
       ↓
Requirement & Skill Extraction
       ↓
Resume–Job Description Comparison
       ↓
Matching Score Calculation
       ↓
Candidate Ranking
       ↓
Recruiter Decision Support
