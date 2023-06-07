/**
Create the tables for the database
for mysql db
* candidate
* status_ref
* user
**/

create table status_ref (
    id int not null,
    status varchar(30) not null,
    primary key (id)
);

CREATE TABLE CandidateStatuses (
  id INT PRIMARY KEY AUTO_INCREMENT,
  status_name VARCHAR(15) NOT NULL unique,
  status_id TINYINT(1) DEFAULT 1
);

CREATE TABLE Trainers (
  id INT PRIMARY KEY AUTO_INCREMENT,
  trainer_name VARCHAR(255) NOT NULL,
  status_id TINYINT(1) DEFAULT 1
);


CREATE TABLE Roles (
  id INT PRIMARY KEY AUTO_INCREMENT,
  role_name VARCHAR(255) NOT NULL,
  status_id TINYINT(1) DEFAULT 1
);

CREATE TABLE Courses (
  id INT PRIMARY KEY AUTO_INCREMENT,
  course_name VARCHAR(255) NOT NULL unique,
  status_id TINYINT(1) DEFAULT 1
);

CREATE TABLE Certifications (
  id INT PRIMARY KEY AUTO_INCREMENT,
  certification_name VARCHAR(255) NOT NULL,
  status_id TINYINT(1) DEFAULT 1
);

CREATE TABLE BGVTeam (
  id INT PRIMARY KEY AUTO_INCREMENT,
  team_name VARCHAR(255) NOT NULL unique,
  status_id TINYINT(1) DEFAULT 1
);

#TODO: change latest_company_worked to latest_company_id
CREATE TABLE Candidates (
  id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  phone VARCHAR(20) NOT NULL,
  bachelors_degree VARCHAR(15),
  bachelors_passout_year_month DATE,
  masters_degree VARCHAR(15),
  masters_passout_year_month DATE,
  host_country_entry_date DATE,
  latest_company_worked VARCHAR(30), 
  total_experience_months INT,
  date_of_birth DATE,
  current_location VARCHAR(255),
  preferred_role VARCHAR(255),
  role_id INT,
  FOREIGN KEY (role_id) REFERENCES Roles(id),
  status_id INT,
  FOREIGN KEY (status_id) REFERENCES CandidateStatuses(id)
);

CREATE TABLE Logins (
  id INT PRIMARY KEY AUTO_INCREMENT,
  candidate_id INT,
  refid VARCHAR(50),
  authentication_type VARCHAR(10),
  FOREIGN KEY (candidate_id) REFERENCES Candidates(id)
);
# insert into logins (candidate_id, refid, authentication_type) values (1, 'roopesht@gmail.com', 'google');
# insert into logins (candidate_id, refid, authentication_type) values (2, 'facebook/roopesht', 'facebook');


create table google_logins (
    id int not null,
    google_id varchar(50) not null,
    primary key (id)
);

create table payment_status_ref (
    id int not null,
    status varchar(15) not null,
    primary key (id)
);

CREATE TABLE Payments (
  id INT PRIMARY KEY AUTO_INCREMENT,
  candidate_id INT,
  due_date DATE NOT NULL,
  amount DECIMAL(10, 2),
  status_id INT,
  installment_number INT default 1, 
  last_communication_date date NULL,

  FOREIGN KEY (candidate_id) REFERENCES Candidates(id),
  FOREIGN KEY (status_id) REFERENCES payment_status_ref(id)

);

create table candidate_certifications (
    id int not null primary key auto_increment,
    candidate_id int not null,
    certification_id int not null,
    foreign key (candidate_id) references candidate (id),
    foreign key (certification_id) references certification (id)
);

create table candidate_courses (
    id int not null primary key auto_increment,
    candidate_id int not null,
    course_id int not null,
    foreign key (candidate_id) references candidate (id),
    foreign key (course_id) references Courses (id)
);


# Role_certifications
# Role_courses

#Audit tables
create table audit_messages (
    id int not null primary key auto_increment,
    candidate_id int not null,
    from_user_id int not null,
    message varchar(255) not null,
    created_at timestamp default current_timestamp
);

# Ref data
# Status, payment_status, roles

# Test data
# Candidates, certifications, courses