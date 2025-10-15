create database clinica2025;
use clinica2025;
create table pacientes(
id_pacientes int auto_increment primary key,
nombre varchar(100),
edad int,
genero varchar(10),
diagnostico varchar(150)
);
insert into pacientes(nombre, edad, genero, diagnostico) 
values('pedro mojica', 19, 'Masculino', 'adiccion');
select * from pacientes;
insert into pacientes(nombre, edad, genero, diagnostico) 
values('Alejandro romero', 19, 'Masculino', 'astigmatismo');

