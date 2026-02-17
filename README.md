# Markowitz-Optimal-Portfolio
# Optimisation de Portefeuille – Modèle de Markowitz (Maximum Sharpe)

## Description

Ce projet implémente une optimisation de portefeuille selon le cadre de Markowitz.

L’objectif est de déterminer les poids optimaux maximisant le ratio de Sharpe sous contraintes.

---

## Cadre théorique

Soit un vecteur de poids w.

Rendement du portefeuille :
E(R_p) = wᵀ μ

Volatilité :
σ_p = √(wᵀ Σ w)

Objectif :

Maximiser Sharpe = E(R_p) / σ_p

Sous contraintes :

- Somme des poids = 1
- Pas de vente à découvert (0 ≤ w ≤ 1)
- Contrainte de volatilité maximale (σ ≤ 12.5%)

---

## Méthodologie

1. Téléchargement des données historiques
2. Calcul des rendements journaliers
3. Annualisation des rendements et covariance
4. Optimisation via méthode SLSQP

---

## Résultats produits

- Poids optimaux
- Rendement attendu
- Volatilité attendue
- Ratio de Sharpe

---

## Intérêt académique

Ce projet illustre :

- L’optimisation quadratique en finance
- L’arbitrage rendement/risque
- L’impact des contraintes sur la solution optimale
- L’utilisation d’algorithmes numériques (SLSQP)

---

## Limites

- Hypothèse de normalité des rendements
- Moyenne et covariance estimées sur historique
- Pas de robustesse face à l’instabilité des paramètres

---

## Extensions possibles

- Frontière efficiente complète
- Optimisation robuste
---

## Auteur

Projet personnel – Optimisation quantitative et théorie moderne du portefeuille.
