drop table if exists candidate_skillset;
drop table if exists candidate_certificates;
drop table if exists candidate;
drop table if exists certificate;
drop table if exists skillset;
 
-- Create the candidate table
CREATE TABLE candidate (
  id INT NOT NULL PRIMARY KEY,
  name VARCHAR(50),
  role VARCHAR(50),
  education VARCHAR(50)
);

-- Insert some sample data into the candidate table
INSERT INTO candidate (id, name, role, education)
VALUES 
    (1, 'John Smith', 'Data Analyst', 'Computer Science'),
    (2, 'Jane Doe', 'Business Intelligence Analyst', 'Business Administration'),
    (3, 'Michael Johnson', 'Data Scientist', 'Statistics'),
    (4, 'Emily Davis', 'Data Engineer', 'Computer Engineering'),
    (5, 'David Wilson', 'Data Visualization Specialist', 'Graphic Design'),
    (6, 'Sarah Thompson', 'Database Administrator', 'Information Systems'),
    (7, 'Robert Brown', 'Data Quality Analyst', 'Data Science');

-- Create the certificate table
CREATE TABLE certificate (
  id INT NOT NULL PRIMARY KEY,
  name VARCHAR(50),
  fee DECIMAL(8, 2)
);

-- Insert some sample data into the certificate table
INSERT INTO certificate (id, name, fee)
VALUES 
    (1, 'Google Certified Data Engineer', 200),
    (2, 'Cloudera Certified Data Analyst', 175),
    (3, 'Microsoft Certified: Azure Administrator Associate', 165),
    (4, 'Google Certified Data Engineer', 200),
    (5, 'Tableau Desktop Certified Associate', 250),
    (6, 'Cloudera Certified Data Analyst', 175),
    (7, 'IBM Certified Data Architect', 180);


-- Create the candidate_certificates table
CREATE TABLE candidate_certificates (
  candidate_id INT NOT NULL,
  certificate_id INT NOT NULL,
  on_date DATE,
  PRIMARY KEY (candidate_id, certificate_id),
  FOREIGN KEY (candidate_id) REFERENCES candidate(id),
  FOREIGN KEY (certificate_id) REFERENCES certificate(id)
);

-- Insert some sample data into the candidate_certificates table
INSERT INTO candidate_certificates (candidate_id, certificate_id, on_date)
VALUES (1, 1, '2022-01-01'),
    	 (2, 2, '2022-02-01'),
    	 (3, 3, '2022-03-01'),
    	 (4, 4, '2022-04-01'),
    	 (5, 5, '2022-05-01'),
    	 (6, 6, '2022-06-01'),
    	 (7, 7, '2022-07-01');

-- Create the skillset table
CREATE TABLE skillset (
  id INT NOT NULL PRIMARY KEY,
  skill_name VARCHAR(50),
  proficiency_level VARCHAR(30)
);

-- Insert some sample data into the skillset table
INSERT INTO skillset (id, skill_name, proficiency_level)
VALUES (123, 'SQL', 'Intermediate'),
    	 (456, 'Python', 'Advanced'),
       (789, 'Data Visualisation', 'Advanced'),
       (213, 'R', 'Intermediate'),
       (546, 'SQL', 'Advanced'),
       (879, 'ETL', 'Intermediate'),
       (321, 'Statistical Analysis', 'Intermediate');

-- Create the candidate_skillset table
CREATE TABLE candidate_skillset (
  candidate_id INT NOT NULL,
  skillset_id INT NOT NULL,
  years_experience INT,
  last_used DATE,
  PRIMARY KEY (candidate_id, skillset_id),
  FOREIGN KEY (candidate_id) REFERENCES candidate(id),
  FOREIGN KEY (skillset_id) REFERENCES skillset(id)
);

-- Insert some sample data into the candidate_skillset table
INSERT INTO candidate_skillset (candidate_id, skillset_id, years_experience, last_used)
VALUES (1, 123, 3, '2023-01-16'),
    	 (2, 456, 4, '2022-09-21'),
       (3, 789, 2, '2023-02-03'),
       (4, 213, 5, '2022-10-17'),
       (5, 546, 3, '2023-03-20'),
       (6, 879, 4, '2022-12-09'),
       (7, 321, 3, '2023-04-25');
