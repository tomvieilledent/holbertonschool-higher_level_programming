# SQL Introduction

Scripts SQL pour les premiers exercices MySQL du projet `holbertonschool-higher_level_programming`.

## Prérequis

- MySQL installé
- Accès à un serveur MySQL local

Exemple de connexion :

```bash
mysql -u root -p
```

## Exécution d'un script

Depuis ce dossier :

```bash
cat 0-list_databases.sql | mysql -u root -p
```

Ou directement :

```bash
mysql -u root -p < 0-list_databases.sql
```

## Liste des tasks

0. `0-list_databases.sql` — List all databases
1. `1-create_database_if_missing.sql` — Create database if it does not exist
2. `2-remove_database.sql` — Delete database if it exists
3. `3-list_tables.sql` — List all tables in a database
4. `4-first_table.sql` — Create first table
5. `5-full_table.sql` — Show table description
6. `6-list_values.sql` — List table rows
7. `7-insert_value.sql` — Insert a new row
8. `8-count_89.sql` — Count rows with a specific value
9. `9-full_creation.sql` — Create and fill a table with data
10. `10-top_score.sql` — List records ordered by score
11. `11-best_score.sql` — Filter records by score
12. `12-no_cheating.sql` — Update score safely
13. `13-change_class.sql` — Remove rows by condition
14. `14-average.sql` — Compute average score
15. `15-groups.sql` — Group records with aggregate

## Notes

- Les scripts sont pensés pour être exécutés individuellement.
- L’ordre de progression conseillé est `0` vers `15`.