-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 19, 2024 at 10:30 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminrecord`
--

CREATE TABLE `adminrecord` (
  `AdminID` varchar(10) NOT NULL,
  `Password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `adminrecord`
--

INSERT INTO `adminrecord` (`AdminID`, `Password`) VALUES
('1', '123'),
('ali ali', 'ali12'),
('mustafa1', '123');

-- --------------------------------------------------------

--
-- Table structure for table `bookrecord`
--

CREATE TABLE `bookrecord` (
  `BookID` varchar(10) NOT NULL,
  `BookName` varchar(35) DEFAULT NULL,
  `Author` varchar(30) DEFAULT NULL,
  `Publisher` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bookrecord`
--

INSERT INTO `bookrecord` (`BookID`, `BookName`, `Author`, `Publisher`) VALUES
('1', 'python', 'ahmed ali', 'dar elhikma'),
('2', 'c++', 'mahamed ali', 'dar elhikma'),
('3', '#C', 'jamal', 'kamal'),
('4', 'Os', 'khaled ahmed', 'dar elhikma'),
('40', 'test', 'test', 'test'),
('5', 'python', 'walid ahmed', 'dar elhikma');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `Feedback` varchar(100) NOT NULL,
  `Rating` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `userrecord`
--

CREATE TABLE `userrecord` (
  `UserID` varchar(255) NOT NULL,
  `UserName` varchar(20) DEFAULT NULL,
  `Password` varchar(20) DEFAULT NULL,
  `BookID` varchar(10) DEFAULT NULL,
  `fines` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userrecord`
--

INSERT INTO `userrecord` (`UserID`, `UserName`, `Password`, `BookID`, `fines`) VALUES
('456', 'mahamed', '741', '2', '10');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adminrecord`
--
ALTER TABLE `adminrecord`
  ADD PRIMARY KEY (`AdminID`);

--
-- Indexes for table `bookrecord`
--
ALTER TABLE `bookrecord`
  ADD PRIMARY KEY (`BookID`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`Feedback`);

--
-- Indexes for table `userrecord`
--
ALTER TABLE `userrecord`
  ADD PRIMARY KEY (`UserID`),
  ADD KEY `BookID` (`BookID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `userrecord`
--
ALTER TABLE `userrecord`
  ADD CONSTRAINT `userrecord_ibfk_1` FOREIGN KEY (`BookID`) REFERENCES `bookrecord` (`BookID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
