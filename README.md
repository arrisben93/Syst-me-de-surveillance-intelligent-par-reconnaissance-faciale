# Projet : Système de Surveillance Intelligent par Reconnaissance Faciale

## Description

Ce projet consiste en le développement d'une **application web de surveillance intelligente**, utilisant la **reconnaissance faciale en temps réel**. Le système exploite une caméra (USB, intégrée ou smartphone) pour détecter, reconnaître et enregistrer les visages des étudiants du cours IA2, à partir d'un fichier de signatures faciales fourni. Lorsqu'un visage inconnu est détecté, une **alarme** est automatiquement déclenchée.

## Fonctionnalités principales

* **Reconnaissance faciale en temps réel** avec affichage du nom ou indication "Inconnu" + alarme.
* **Gestion des visages inconnus** avec notifications visuelles et/ou sonores.
* **Enregistrement des détections** dans une base de données (SQLite).
* **Interface web sécurisée** avec tableau de bord pour consulter l'historique et des statistiques simples.

## Technologies utilisées

* **Python** (OpenCV, face\_recognition)
* **SQLite** (base de données)
* **Streamlit** (interface web et dashboard)
* **Caméra physique ou virtuelle** (Webcam, IP cam...)

## Architecture du projet

* 📷 **Module de détection** (connexion caméra, reconnaissance faciale, gestion des alarmes)
* 🛢️ **Base de données** (nom, date, heure, type de détection)
* 🖥️ **Dashboard** (visualisation des détections, statistiques, filtrage)
* 🔐 **Page d'authentification** (accès sécurisé au dashboard)

## Installation
pip install -r requirements.txt

## Lancer la surveillance
python app.py

## Lancer le dashboard
streamlit run interface_web.py

## Identifiants
Username : Ariss
Password : 2000

