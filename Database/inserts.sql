INSERT INTO `tfgBBDD`.`Deporte`
(`ID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(1,
'Fútbol',
current_time(),
current_time());


INSERT INTO `tfgBBDD`.`Deporte`
(`ID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(2,
'Balonmán',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Federacion`
(`ID`,
`Nome`,
`deporteID`,
`created_at`,
`updated_at`)
VALUES
(101,
'Federación Galega de Fútbol',
1,
current_time(),
current_time());


INSERT INTO `tfgBBDD`.`Federacion`
(`ID`,
`Nome`,
`deporteID`,
`created_at`,
`updated_at`)
VALUES
(102,
'Real Federación Andaluza de Fútbol',
1,
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Federacion`
(`ID`,
`Nome`,
`deporteID`,
`created_at`,
`updated_at`)
VALUES
(103,
'Federación Cántabra de Fútbol',
1,
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Federacion`
(`ID`,
`Nome`,
`deporteID`,
`created_at`,
`updated_at`)
VALUES
(104,
'Federación de Fútbol de Ceuta',
1,
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Federacion`
(`ID`,
`Nome`,
`deporteID`,
`created_at`,
`updated_at`)
VALUES
(105,
'Federación de Fútbol de Castilla la Mancha',
1,
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Federacion`
(`ID`,
`Nome`,
`deporteID`,
`created_at`,
`updated_at`)
VALUES
(106,
'Real Federación de Fútbol de Madrid',
1,
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Federacion`
(`ID`,
`Nome`,
`deporteID`,
`created_at`,
`updated_at`)
VALUES
(107,
'Federación Riojana de Fútbol',
1,
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Federacion`
(`ID`,
`Nome`,
`deporteID`,
`created_at`,
`updated_at`)
VALUES
(108,
'Federación Aragonesa de Fútbol',
1,
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Federacion`
(`ID`,
`Nome`,
`deporteID`,
`created_at`,
`updated_at`)
VALUES
(109,
'Federación Extremeña de Fútbol',
1,
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Federacion`
(`ID`,
`Nome`,
`deporteID`,
`created_at`,
`updated_at`)
VALUES
(110,
'Federación de Fútbol de la Región de Murcia',
1,
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Federacion`
(`ID`,
`Nome`,
`deporteID`,
`created_at`,
`updated_at`)
VALUES
(201,
'Real Federación Española de Balonmano',
2,
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Federacion`
(`ID`,
`Nome`,
`deporteID`,
`created_at`,
`updated_at`)
VALUES
(202,
'Federación Galega de Balonmán',
2,
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Federacion`
(`ID`,
`Nome`,
`deporteID`,
`created_at`,
`updated_at`)
VALUES
(203,
'Federació Catalana d\'Handbol',
2,
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(1,
102,
'Cadete: División de Honor',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(2,
102,
'Segunda Divisón Femenina Andaluza: Almería',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(3,
103,
'Juvenil: Divisón Nacional',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(4,
103,
'Amateur: Preferente',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(5,
104,
'Amateur Fútbol Sala: Tercera División, Grupo 22',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(6,
104,
'Infantil: Liga Regular',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(7,
101,
'Cadete: Liga Galega',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(8,
101,
'Feminino: Segunda Dvisión',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(9,
106,
'Juvenil: Primera División Nacional',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(10,
106,
'Amateur: Preferente, Grupo 1',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(11,
107,
'Amateur: Tercera División, Grupo 16',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(12,
107,
'Femenino: Primera Nacional, Grupo 2',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(13,
105,
'Juvenil Fútbol Sala: División de Honor, Grupo 4',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(14,
105,
'Juvenil Fútbol Sala: División de Honor, Grupo 4',
current_time(),
current_time());


INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(15,
108,
'Infantil: Primera División, Grupo 1',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(16,
108,
'Amateur: Preferente, Grupo 1',
current_time(),
current_time());


INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(17,
109,
'Femenino: Primera División, Iberitos.',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(18,
109,
'Juvenil: División de Honor.',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(19,
110,
'Futbol Sala Femenino: Segunda División',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(20,
203,
'Femenino: Primera División',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(21,
203,
'Infantil: Lliga Catalana',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(22,
202,
'Amateur: Primera División',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(23,
202,
'Xuvenil: División de Honra',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(24,
201,
'Amateur: Primera División, Grupo A',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(25,
201,
'Femenino: División de Honor',
current_time(),
current_time());

INSERT INTO `tfgBBDD`.`Competicion`
(`ID`,
`federacionID`,
`Nome`,
`created_at`,
`updated_at`)
VALUES
(26,
101,
'Amateur: Segunda Rexional, Grupo 1: A Coruña',
current_time(),
current_time());
