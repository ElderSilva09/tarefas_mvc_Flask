DROP DATABASE IF EXISTS `tarefas`

CREATE DATABASE IF NOT EXISTS `tarefas`;

USE `tarefas`;

DROP TABLE IF EXISTS `tarefas`;

CREATE TABLE IF NOT EXISTES `tarefas`; (
    'id_tarefa' INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `titulo_tarefa` VARCHAR(100) NOT NULL,
    'data-conclusao' DATETIME NULL
);

