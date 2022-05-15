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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (22,'contenttypes','0001_initial','2022-04-18 12:27:35.348667'),(23,'auth','0001_initial','2022-04-18 12:27:35.353749'),(24,'admin','0001_initial','2022-04-18 12:27:35.357294'),(25,'admin','0002_logentry_remove_auto_add','2022-04-18 12:27:35.361294'),(26,'admin','0003_logentry_add_action_flag_choices','2022-04-18 12:27:35.364304'),(27,'contenttypes','0002_remove_content_type_name','2022-04-18 12:27:35.367293'),(28,'auth','0002_alter_permission_name_max_length','2022-04-18 12:27:35.370603'),(29,'auth','0003_alter_user_email_max_length','2022-04-18 12:27:35.373592'),(30,'auth','0004_alter_user_username_opts','2022-04-18 12:27:35.378592'),(31,'auth','0005_alter_user_last_login_null','2022-04-18 12:27:35.382355'),(32,'auth','0006_require_contenttypes_0002','2022-04-18 12:27:35.385345'),(33,'auth','0007_alter_validators_add_error_messages','2022-04-18 12:27:35.388599'),(34,'auth','0008_alter_user_username_max_length','2022-04-18 12:27:35.392604'),(35,'auth','0009_alter_user_last_name_max_length','2022-04-18 12:27:35.395603'),(36,'auth','0010_alter_group_name_max_length','2022-04-18 12:27:35.398603'),(37,'auth','0011_update_proxy_permissions','2022-04-18 12:27:35.401663'),(38,'auth','0012_alter_user_first_name_max_length','2022-04-18 12:27:35.404663'),(40,'sessions','0001_initial','2022-04-18 12:27:35.411665'),(58,'login1','0001_initial','2022-04-22 05:18:10.318659'),(59,'login1','0002_alter_tbl_authentication_loginid','2022-04-22 05:18:10.325084'),(60,'login1','0003_alter_tbl_authentication_managers','2022-04-22 05:18:10.329907'),(61,'login1','0004_alter_tbl_authentication_managers','2022-04-22 05:18:10.332908'),(62,'login1','0005_alter_tbl_authentication_managers','2022-04-22 05:18:10.336303'),(63,'login1','0006_tbl_authentication_role','2022-04-22 05:18:10.341546'),(64,'login1','0007_student_data','2022-04-22 05:18:10.345547'),(65,'login1','0008_alter_student_data_username','2022-04-22 05:18:10.348204'),(66,'login1','0009_alter_student_data_department','2022-04-22 05:18:10.351204'),(67,'login1','0010_rename_department_student_data_department','2022-04-22 05:18:10.354204'),(68,'login1','0011_rename_book1_student_data_book1_and_more','2022-04-22 05:18:10.358233'),(69,'login1','0012_books_history','2022-04-22 05:18:10.361191'),(70,'login1','0013_book_history','2022-04-22 05:18:10.364670'),(71,'login1','0014_librarian_data','2022-04-22 05:18:18.189648'),(72,'login1','0015_alter_librarian_data_lib_age_and_more','2022-04-22 05:18:18.197183'),(73,'login1','0016_books_data','2022-04-25 10:51:48.928656'),(74,'login1','0017_remove_books_data_id_alter_books_data_book_id','2022-04-25 10:54:02.844447'),(75,'login1','0018_alter_books_data_book_id','2022-04-25 10:58:27.561375'),(76,'login1','0020_alter_student_data_book1_alter_student_data_book2_and_more','2022-04-27 06:02:35.093083');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
