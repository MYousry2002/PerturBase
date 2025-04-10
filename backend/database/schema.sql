CREATE TABLE Experiment (
    ExpID INT NOT NULL AUTO_INCREMENT,
    Name VARCHAR(128),
    Date DATE,
    Treatment VARCHAR(128),
    Source VARCHAR(128),
    Publication VARCHAR(128),
    PRIMARY KEY(ExpID)
) engine = innodb;

CREATE TABLE ChannelMetaData (
    CMID INT NOT NULL AUTO_INCREMENT,
    ExpID INT,
    Type ENUM('RNA', 'sgRNA', 'ADT'),
    Ncells INT,
    Nfeatures_avg INT,
    Ncount_avg INT,
    Mito_avg FLOAT,
    Ribo_avg FLOAT,
    nFeature_avg_cite INT,
    nCount_avg_cite INT,
    PRIMARY KEY(CMID)
    FOREIGN KEY (ExpID) REFERENCES Experiment(ExpID)
) engine = innodb;

CREATE TABLE ChannelCounts (
    CountID INT NOT NULL AUTO_INCREMENT,
    CMID INT,
    Cell_Name VARCHAR(128),
    Feature VARCHAR(128),
    Count INT,
    PRIMARY KEY(CountID)
    FOREIGN KEY (CMID) REFERENCES ChannelMetaData(CMID),
) engine = innodb;

CREATE TABLE RawCounts (
    RawID INT NOT NULL AUTO_INCREMENT,
    ExpID INT,
    Matrix_File VARCHAR(256),
    PRIMARY KEY(RawID)
    FOREIGN KEY (ExpID) REFERENCES Experiment(ExpID)
); engine = innodb;
