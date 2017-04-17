/*
 
 Source Server Type    : MySQL
 Source Server Version : 50717
 Source Host           : localhost
 Source Database       : enroll-analytics

 Target Server Type    : MySQL
 Target Server Version : 50717
 File Encoding         : utf-8

*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `courses`
-- ----------------------------
DROP TABLE IF EXISTS `courses`;
CREATE TABLE `courses` (
  `pk` int(11) NOT NULL,
  `dept` varchar(6) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `title` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`pk`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `courses`
-- ----------------------------
BEGIN;
INSERT INTO `courses` VALUES ('1', '\'CS\'', '101', '\'Living with Computers\''), ('2', '\'CS\'', '135', '\'Select Top in Comp Science\''), ('3', '\'CS\'', '144', '\'Intro to Computer Science\''), ('4', '\'CS\'', '145', '\'Intro to Object-Oriented Prog\''), ('5', '\'CS\'', '235', '\'Select Top in Comp Science\''), ('6', '\'CS\'', '245', '\'Adv Computer Programming\''), ('7', '\'CS\'', '418', '\'Multimedia Programming\''), ('8', '\'CS\'', '451', '\'Software Engineering\''), ('9', '\'CS\'', '456', '\'Internet Services\''), ('10', '\'CS\'', '457', '\'Computer Networks\'');
COMMIT;

-- ----------------------------
--  Table structure for `schedules`
-- ----------------------------
DROP TABLE IF EXISTS `schedules`;
CREATE TABLE `schedules` (
  `pk` int(11) NOT NULL,
  `course_pk` int(11) NOT NULL,
  `semester_pk` int(11) NOT NULL,
  `crn` int(11) NOT NULL,
  `type` varchar(48) NOT NULL,
  `section` int(11) NOT NULL,
  `max_enroll` int(11) NOT NULL,
  `actual_enroll` int(11) NOT NULL,
  PRIMARY KEY (`pk`),
  KEY `course_pk` (`course_pk`),
  KEY `semester_pk` (`semester_pk`),
  CONSTRAINT `schedules_ibfk_1` FOREIGN KEY (`course_pk`) REFERENCES `courses` (`pk`),
  CONSTRAINT `schedules_ibfk_2` FOREIGN KEY (`semester_pk`) REFERENCES `semesters` (`pk`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `schedules`
-- ----------------------------
BEGIN;
INSERT INTO `schedules` VALUES ('1', '1', '1', '2509', '\'Lecture\'', '1', '40', '39'), ('2', '7', '2', '2510', '\'Lecture\'', '2', '40', '37'), ('3', '8', '5', '2511', '\'Lecture\'', '3', '20', '19'), ('4', '9', '9', '2512', '\'Lecture\'', '4', '20', '17'), ('5', '10', '10', '2513', '\'Lecture\'', '5', '20', '20'), ('6', '1', '15', '2514', '\'Lecture\'', '6', '20', '20'), ('7', '2', '16', '3349', '\'Lecture\'', '1', '25', '16'), ('8', '3', '22', '2501', '\'Lecture\'', '1', '25', '14'), ('9', '3', '20', '2502', '\'Lecture\'', '2', '25', '14'), ('10', '4', '19', '2491', '\'Lecture\'', '1', '25', '7');
COMMIT;

-- ----------------------------
--  Table structure for `semesters`
-- ----------------------------
DROP TABLE IF EXISTS `semesters`;
CREATE TABLE `semesters` (
  `pk` int(11) NOT NULL,
  `code` int(11) DEFAULT NULL,
  `title` varchar(48) DEFAULT NULL,
  PRIMARY KEY (`pk`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `semesters`
-- ----------------------------
BEGIN;
INSERT INTO `semesters` VALUES ('1', '200610', '\'Fall Semester 2005\''), ('2', '200620', '\'Spring Semester 2006\''), ('3', '200630', '\'Summer Semester 2006\''), ('4', '200710', '\'Fall Semester 2006\''), ('5', '200720', '\'Spring Semester 2007\''), ('6', '200730', '\'Summer Semester 2007\''), ('7', '200810', '\'Fall Semester 2007\''), ('8', '200820', '\'Spring Semester 2008\''), ('9', '200830', '\'Summer Semester 2008\''), ('10', '200910', '\'Fall Semester 2008\''), ('11', '200920', '\'Spring Semester 2009\''), ('12', '200930', '\'Summer Semester 2009\''), ('13', '201010', '\'Fall Semester 2009\''), ('14', '201020', '\'Spring Semester 2010\''), ('15', '201030', '\'Summer Semester 2010\''), ('16', '201110', '\'Fall Semester 2010\''), ('17', '201120', '\'Spring Semester 2011\''), ('18', '201130', '\'Summer Semester 2011\''), ('19', '201210', '\'Fall Semester 2011\''), ('20', '201220', '\'Spring Semester 2012\''), ('21', '201230', '\'Summer Semester 2012\''), ('22', '201310', '\'Fall Semester 2012\''), ('23', '201320', '\'Spring Semester 2013\''), ('24', '201330', '\'Summer Semester 2013\''), ('25', '201410', '\'Fall Semester 2013\''), ('26', '201420', '\'Spring Semester 2014\''), ('27', '201430', '\'Summer Semester 2014\''), ('28', '201510', '\'Fall Semester 2014\''), ('29', '201520', '\'Spring Semester 2015\''), ('30', '201610', '\'Fall Semester 2015\'');
COMMIT;

-- ----------------------------
--  View structure for `composite_join_view`
-- ----------------------------
DROP VIEW IF EXISTS `composite_join_view`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `composite_join_view` AS select `schedules`.`semester_pk` AS `semester_pk`,`courses`.`title` AS `title` from (`schedules` left join `courses` on((`schedules`.`course_pk` = `courses`.`pk`)));

-- ----------------------------
--  View structure for `left_outer_view`
-- ----------------------------
DROP VIEW IF EXISTS `left_outer_view`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `left_outer_view` AS select `semesters`.`title` AS `title`,`schedules`.`semester_pk` AS `semester_pk` from (`semesters` left join `schedules` on((`schedules`.`course_pk` = `semesters`.`pk`)));

-- ----------------------------
--  View structure for `natural_join_view`
-- ----------------------------
DROP VIEW IF EXISTS `natural_join_view`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `natural_join_view` AS select `schedules`.`semester_pk` AS `semester_pk`,`courses`.`title` AS `title` from (`schedules` left join `courses` on((`schedules`.`course_pk` = `courses`.`pk`)));

-- ----------------------------
--  View structure for `right_outer_view`
-- ----------------------------
DROP VIEW IF EXISTS `right_outer_view`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `right_outer_view` AS select `schedules`.`semester_pk` AS `semester_pk`,`semesters`.`title` AS `title` from (`semesters` left join `schedules` on((`schedules`.`course_pk` = `semesters`.`pk`))) where isnull(`schedules`.`semester_pk`);

-- ----------------------------
--  View structure for `untaught_courses_view`
-- ----------------------------
DROP VIEW IF EXISTS `untaught_courses_view`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `untaught_courses_view` AS select `schedules`.`semester_pk` AS `semester_pk`,`courses`.`title` AS `title` from (`courses` left join `schedules` on((`schedules`.`course_pk` = `courses`.`pk`))) where isnull(`schedules`.`semester_pk`);

SET FOREIGN_KEY_CHECKS = 1;
