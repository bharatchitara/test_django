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
-- Table structure for table `login1_books_data`
--

DROP TABLE IF EXISTS `login1_books_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login1_books_data` (
  `book_name` varchar(40) NOT NULL,
  `book_id` int NOT NULL,
  `book_author` varchar(30) NOT NULL,
  `total_count` int NOT NULL,
  `description` varchar(200) NOT NULL,
  `department` int NOT NULL,
  `location` int NOT NULL,
  PRIMARY KEY (`book_id`),
  UNIQUE KEY `book_name` (`book_name`),
  UNIQUE KEY `login1_books_data_book_id_71692aa2_uniq` (`book_id`),
  KEY `department` (`department`),
  CONSTRAINT `login1_books_data_ibfk_1` FOREIGN KEY (`department`) REFERENCES `departments` (`value`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login1_books_data`
--

LOCK TABLES `login1_books_data` WRITE;
/*!40000 ALTER TABLE `login1_books_data` DISABLE KEYS */;
INSERT INTO `login1_books_data` VALUES ('Concept of physics part1',1001,'H.C. Verma',35,'Physics part1',1,1),('Concept of physics part2',1002,'H.C. Verma',20,'Physics part2',1,3),('test book',1003,'gje',23,'sdas',1,1),('new test ',1004,'wer',23,'wre',1,2),('new test 1',1005,'gje',34,'asda',1,2),('sd',1006,'as',23,'sd',1,1),('s',1007,'rkre',23,'asd',1,2),('sd22',1008,'sd',333,'asd',1,2),('petter',1009,'asd',3,'er',1,3),('asa',1010,'asd',2,'x',1,2),('petter1',1011,'Test author',34,'asdbja',1,3),('qweweqwe',1012,'ss',12,'asd',1,2),('adsddsdvf',1013,'asdasd',2,'asd',1,2),('ssdsdccoo',1014,'asd',22,'asd',1,2),('Indian history',2001,'PK. Sharma',100,'NCERT history class 12th',2,1),('NCERT microeconomics',3001,'NCERT',30,'economics',3,2),('NCERT microeconomics part2  ',3002,'NCERT',30,'economics part2 ',3,4),('harry potter part1 ',4001,'JK Rowling',10,'fiction',4,2),('harry potter part2',4002,'JK Rowling',12,'fiction',4,2),('new test 87',4003,'gje',23,'wq',4,3);
/*!40000 ALTER TABLE `login1_books_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-06 18:06:30
