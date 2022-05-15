-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: library_management
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `login1_student_data`
--

DROP TABLE IF EXISTS `login1_student_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login1_student_data` (
  `username` varchar(50) NOT NULL,
  `name` varchar(60) NOT NULL,
  `age` int DEFAULT NULL,
  `gender` varchar(1) NOT NULL,
  `department` int NOT NULL,
  `book1` varchar(200) DEFAULT NULL,
  `book2` varchar(200) DEFAULT NULL,
  `book3` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`username`),
  KEY `login1_student_data_ibfk_1` (`department`),
  CONSTRAINT `login1_student_data_ibfk_1` FOREIGN KEY (`department`) REFERENCES `departments` (`value`),
  CONSTRAINT `check_age1` CHECK ((`age` <= 99))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login1_student_data`
--

LOCK TABLES `login1_student_data` WRITE;
/*!40000 ALTER TABLE `login1_student_data` DISABLE KEYS */;
INSERT INTO `login1_student_data` VALUES ('bharatc@spanidea.com','Bharat chitarart',28,'M',1,'NCERT physics part1','harry potter part1','NCERT English class 12 part1'),('stu1@spanidea.com','peter',23,'M',2,'Concept of Physics','political science class 12th','NCERT Hindi'),('stu2@spanidea.com','my student ',24,'M',4,'','',''),('stu@spanidea.com','Ram',23,'M',1,'Concept of physics part1','new test ','NCERT microeconomics part2  ');
/*!40000 ALTER TABLE `login1_student_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-06 18:06:28
