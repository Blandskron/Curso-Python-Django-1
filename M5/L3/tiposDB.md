## 🟦 BASES DE DATOS SQL (Relacionales)

👉 **Modelo estructurado**, esquemas rígidos, ACID, ideal para datos críticos.

### 🔹 PostgreSQL

* **Tipo:** SQL relacional avanzada
* **Herramientas:** pgAdmin, DBeaver, DataGrip
* **Usos típicos:**
  Sistemas financieros, ERP, SaaS, microservicios, analytics, GIS (PostGIS)

---

### 🔹 MySQL

* **Tipo:** SQL relacional
* **Herramientas:** MySQL Workbench, DBeaver, phpMyAdmin
* **Usos típicos:**
  Aplicaciones web, CMS (WordPress), e-commerce, backend clásico

---

### 🔹 MariaDB

* **Tipo:** SQL (fork de MySQL)
* **Herramientas:** DBeaver, HeidiSQL
* **Usos típicos:**
  Hosting, reemplazo de MySQL, proyectos open source

---

### 🔹 SQL Server

* **Tipo:** SQL relacional empresarial
* **Herramientas:** SSMS, Azure Data Studio
* **Usos típicos:**
  Sistemas corporativos, BI, entornos Microsoft

---

### 🔹 Oracle Database

* **Tipo:** SQL relacional empresarial
* **Herramientas:** Oracle SQL Developer
* **Usos típicos:**
  Bancos, gobiernos, grandes corporaciones

---

### 🔹 SQLite

* **Tipo:** SQL embebido
* **Herramientas:** DB Browser for SQLite
* **Usos típicos:**
  Apps móviles, prototipos, testing, desktop apps

---

### 🔹 IBM Db2

* **Tipo:** SQL empresarial
* **Herramientas:** Db2 Data Studio
* **Usos típicos:**
  Mainframes, grandes industrias

---

## 🟩 BASES DE DATOS NoSQL

👉 **Flexibilidad**, escalabilidad horizontal, grandes volúmenes o baja latencia.

---

## 📄 NoSQL — Documentales

### 🔹 MongoDB

* **Modelo:** Documentos (JSON/BSON)
* **Herramientas:** MongoDB Compass
* **Usos típicos:**
  APIs REST, microservicios, apps con esquemas variables

---

### 🔹 CouchDB

* **Modelo:** Documentos
* **Herramientas:** Fauxton
* **Usos típicos:**
  Sincronización offline, apps distribuidas

---

## 🔑 NoSQL — Clave-Valor

### 🔹 Redis

* **Modelo:** Key-Value (en memoria)
* **Herramientas:** RedisInsight
* **Usos típicos:**
  Cache, sesiones, colas, rate-limit, pub/sub

---

### 🔹 Amazon DynamoDB

* **Modelo:** Key-Value / Document
* **Herramientas:** AWS Console
* **Usos típicos:**
  Serverless, alta escalabilidad, IoT

---

## 📊 NoSQL — Columnas (Wide Column)

### 🔹 Cassandra

* **Modelo:** Columnas distribuidas
* **Herramientas:** DataStax Studio
* **Usos típicos:**
  Big Data, alta disponibilidad, logs masivos

---

### 🔹 HBase

* **Modelo:** Columnas
* **Herramientas:** Apache HBase UI
* **Usos típicos:**
  Hadoop, procesamiento masivo

---

## 🕸️ NoSQL — Grafos

### 🔹 Neo4j

* **Modelo:** Grafos
* **Herramientas:** Neo4j Browser, Bloom
* **Usos típicos:**
  Redes sociales, relaciones complejas, fraude

---

### 🔹 Amazon Neptune

* **Modelo:** Grafo
* **Usos típicos:**
  Knowledge graphs, relaciones semánticas

---

## ⏱️ NoSQL — Series de Tiempo

### 🔹 InfluxDB

* **Modelo:** Time Series
* **Herramientas:** Influx UI
* **Usos típicos:**
  IoT, métricas, monitoreo, DevOps

---

### 🔹 TimescaleDB

* **Modelo:** Time Series sobre PostgreSQL
* **Herramientas:** pgAdmin, Grafana
* **Usos típicos:**
  Observabilidad, datos temporales

---

## 🔍 NoSQL — Búsqueda / Indexación

### 🔹 Elasticsearch

* **Modelo:** Índices distribuidos
* **Herramientas:** Kibana
* **Usos típicos:**
  Búsquedas, logs, analytics, observabilidad

---

### 🔹 OpenSearch

* **Modelo:** Search engine
* **Herramientas:** OpenSearch Dashboards
* **Usos típicos:**
  Logs, búsquedas, reemplazo open-source de Elastic

---

## 🧠 BASES DE DATOS ESPECIALES / MODERNAS

### 🔹 Firebase Firestore

* **Modelo:** Documental en tiempo real
* **Usos típicos:**
  Apps móviles, realtime sync, startups

---

### 🔹 Supabase

* **Modelo:** PostgreSQL + servicios
* **Usos típicos:**
  Backend rápido, SaaS, prototipos

---

### 🔹 Snowflake

* **Modelo:** Data Warehouse
* **Usos típicos:**
  BI, analytics, big data empresarial

---

### 🔹 ClickHouse

* **Modelo:** Columnar analítico
* **Usos típicos:**
  Analytics en tiempo real, grandes volúmenes

---

## 🛠️ HERRAMIENTAS UNIVERSALES (Multi-DB)

Estas trabajan con **SQL y NoSQL**:

* **DBeaver** → multi-DB, open source
* **DataGrip** → JetBrains, profesional
* **TablePlus** → liviano y moderno
* **Navicat** → comercial, multiplataforma

---

## 📌 RESUMEN RÁPIDO DE ELECCIÓN

| Necesidad              | Recomendación          |
| ---------------------- | ---------------------- |
| Transacciones críticas | PostgreSQL             |
| Web tradicional        | MySQL / MariaDB        |
| Cache / performance    | Redis                  |
| Esquemas flexibles     | MongoDB                |
| Relaciones complejas   | Neo4j                  |
| Logs / búsqueda        | Elasticsearch          |
| Tiempo real / métricas | InfluxDB               |
| Mobile / offline       | Firebase               |
| Analytics masivo       | ClickHouse / Snowflake |
