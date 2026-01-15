CREATE TABLE alumno (
    id_alumno SERIAL PRIMARY KEY,
    rut VARCHAR(12) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(150) NOT NULL UNIQUE
);

CREATE TABLE cursos (
    id_curso SERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    docente VARCHAR(100) NOT NULL
);

CREATE TABLE matricula (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    id_alumno INT NOT NULL,
    CONSTRAINT fk_matricula_alumno
        FOREIGN KEY (id_alumno)
        REFERENCES alumno(id_alumno)
        ON DELETE CASCADE
);

CREATE TABLE alumno_curso (
    id SERIAL PRIMARY KEY,
    id_alumno INT NOT NULL,
    id_curso INT NOT NULL,
    CONSTRAINT fk_alumno_curso_alumno
        FOREIGN KEY (id_alumno)
        REFERENCES alumno(id_alumno)
        ON DELETE CASCADE,
    CONSTRAINT fk_alumno_curso_curso
        FOREIGN KEY (id_curso)
        REFERENCES cursos(id_curso)
        ON DELETE CASCADE,
    CONSTRAINT uq_alumno_curso UNIQUE (id_alumno, id_curso)
);
