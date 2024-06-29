import json

response = '''
{
    "status": "finProcess",
    "nbQuestion": "3 / 20",
    "projets": [
        {
            "cahierDesCharges": {
                "titre": "Mise en place d'une plateforme de gestion des stocks intégrée",
                "description": "Ce projet vise à mettre en place une plateforme de gestion des stocks intégrée et automatisée pour optimiser la gestion de vos produits et réduire les risques d'erreurs.",
                "noteSur100": "85%",
                "justificationNote": "Ce projet est essentiel pour améliorer l'efficacité opérationnelle de votre entreprise, réduire les coûts liés aux erreurs de stock et offrir une meilleure expérience client.",
                "tempsProjet": "3 mois",
                "prixGlobal": "30 000€",
                "prixGlobalConcurrents": "45 000€",
                "taches": [
                    {
                        "titreTache": "Analyse des besoins en stock",
                        "posteTache": "Freelance junior",
                        "descriptionTache": "Identifier les besoins spécifiques de votre entreprise en termes de gestion des stocks.",
                        "tempsTache": "1 semaine",
                        "prixTache": "500€",
                        "prixTacheConcurrents": "800€"
                    },
                    {
                        "titreTache": "Mise en place de la plateforme",
                        "posteTache": "Freelance senior",
                        "descriptionTache": "Développer et mettre en place la plateforme de gestion des stocks intégrée.",
                        "tempsTache": "2 mois",
                        "prixTache": "20 000€",
                        "prixTacheConcurrents": "30 000€"
                    },
                    {
                        "titreTache": "Formation des utilisateurs",
                        "posteTache": "Freelance junior",
                        "descriptionTache": "Former les employés à l'utilisation de la nouvelle plateforme de gestion des stocks.",
                        "tempsTache": "2 semaines",
                        "prixTache": "1 500€",
                        "prixTacheConcurrents": "2 000€"
                    }
                ]
            }
        },
        {
            "cahierDesCharges": {
                "titre": "Mise en place d'un système d'analyse avancée pour la chaîne d'approvisionnement",
                "description": "Ce projet consiste à mettre en place un système d'analyse avancée des données pour optimiser votre chaîne d'approvisionnement et améliorer la gestion des stocks.",
                "noteSur100": "90%",
                "justificationNote": "Ce projet est crucial pour améliorer l'efficacité opérationnelle de votre entreprise et réduire les coûts liés à la gestion des stocks.",
                "tempsProjet": "4 mois",
                "prixGlobal": "40 000€",
                "prixGlobalConcurrents": "55 000€",
                "taches": [
                    {
                        "titreTache": "Analyse des besoins en analyse de données",
                        "posteTache": "Freelance junior",
                        "descriptionTache": "Identifier les besoins spécifiques de votre entreprise en termes d'analyse avancée pour la chaîne d'approvisionnement.",
                        "tempsTache": "1 semaine",
                        "prixTache": "500€",
                        "prixTacheConcurrents": "800€"
                    },
                    {
                        "titreTache": "Développement du système d'analyse avancée",
                        "posteTache": "Freelance senior",
                        "descriptionTache": "Concevoir et mettre en place le système d'analyse avancée pour la chaîne d'approvisionnement.",
                        "tempsTache": "3 mois",
                        "prixTache": "30 000€",
                        "prixTacheConcurrents": "40 000€"
                    },
                    {
                        "titreTache": "Formation des utilisateurs",
                        "posteTache": "Freelance junior",
                        "descriptionTache": "Former les employés à l'utilisation du système d'analyse avancée.",
                        "tempsTache": "1 mois",
                        "prixTache": "2 500€",
                        "prixTacheConcurrents": "3 000€"
                    }
                ]
            }
        }
    ]
}
'''

respJSON = json.loads(response)

for projet in respJSON["projets"]:
    cdc = projet['cahierDesCharges']
    print(cdc["titre"])