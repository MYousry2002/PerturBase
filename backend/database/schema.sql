CREATE TABLE Experiment (
    ExpID INT PRIMARY KEY,
    Name VARCHAR(128),
    Date DATE,
    Treatment VARCHAR(128),
    Source VARCHAR(128),
    Publication VARCHAR(128)
);

CREATE TABLE ChannelMetaData (
    CMID INT PRIMARY KEY,
    ExpID INT,
    Type ENUM('RNA', 'sgRNA', 'ADT'),
    Ncells INT,
    Nfeatures_avg INT,
    Ncount_avg INT,
    Mito_avg FLOAT,
    Ribo_avg FLOAT,
    nFeature_avg_cite INT,
    nCount_avg_cite INT,
    FOREIGN KEY (ExpID) REFERENCES Experiment(ExpID)
);

CREATE TABLE ChannelCounts (
    CountID INT PRIMARY KEY,
    CMID INT,
    Cell_Name VARCHAR(128),
    Feature VARCHAR(128),
    Count INT,
    FOREIGN KEY (CMID) REFERENCES ChannelMetaData(CMID),
    INDEX idx_feature (Feature)
);

CREATE TABLE RawCounts (
    RawID INT PRIMARY KEY,
    ExpID INT,
    Matrix_File VARCHAR(256),
    FOREIGN KEY (ExpID) REFERENCES Experiment(ExpID)
);