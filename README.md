# Team4_Capstone NYC Job Posting Data Analysis

 Overview:
 This project involves analyzing job market posting data from the City of New York's official job sight to gain insights into the job market landscape. The goal of this project is to explore trends, identify key insights and visualize the data to provide valuable information for candidates, employers and staffing agencies. 

 Dataset:
 The dataset is sourced from: 
 https://catalog.data.gov/dataset/nyc-jobs

 It includes information about job postings available to both city employees and the general public. 
 It contains the following fields:
    job_id: Unique identifier for each job posting
    agency_posting_type: Indicates whether the posting is internal (for city employees) or external (for the general public)
    num_pos: Number of positions available for the job posting
    business_title: Title of the job
    civil_title: Civil service title (if applicable)
    level: Job level (e.g., entry-level, mid-level, senior-level)
    category: Job category or industry
    ft_pt: Full-time or part-time position
    career_level: Career level of the position (e.g., executive, managerial, professional)
    yearly_salary: Yearly salary for the position (if available)
    ocation: Location of the job
    division: Division or department within the organization
    _min_qual: Minimum qualifications required for the position
    res_req: Additional job requirements or responsibilities
    ost_date: Date when the job posting was posted

 Analysis and Visualization:
    Job Market Trends:
        Analyse the distribution of the job postings over time to identify seasonal trends
    Salary Analysis:
        Calculate descriptive statistics for yearly salaries for comparison
    Job Type Analysis:
        Explore the distribution of internal and external available positions
    Career Level Analysis:
        Investigate the distribution of job postings by career level to understand the availability
    Correlation Analysis:
        Explore potental correlations between attribtes such as location, salary and category to uncover factors that may influence the hiring decision and compensation levels. 

 Usage:
  To run the code:
        1. pip install:
            pandas, numpy, seaborn, sqlite3, matplotlib, sqlalchemy

  Dowload the dataset and save it as a SQLite database file named "CAPSTONE_db.db"

  Run the provided python scripts to generate the analysis

 
 Contributors:
 Gabrielle Glasgow
 Max Ross
 Jason Fearnall





