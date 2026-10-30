CREATE DATABASE IF NOT EXISTS `tarefas`;

USE `tarefas`;

CREATE TABLE IF NOT EXISTS `tarefas` (
    `id_tarefa` BIGINT NOT NULL AUTO_INCRMENT PRIMARY KEY,
    `titulo_tarefa` VARCHAR(100) NOT NULL,
    `data_conclusao` DATETIME NULL
);

