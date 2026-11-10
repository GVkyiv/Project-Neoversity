---
title: "MLOps CI/CD"
---

# MLOps CI/CD

Tier 2. Фінальний результат: повний MLOps-конвеєр: Docker, K8s (EKS),
Terraform, Helm/ArgoCD, Prometheus/Grafana, MLflow.

## База знань: Лекції та матеріали курсу

### Вступ та операційна база
- [Вступ до курсу: програма, артефакти та фінальний проєкт](lectures/00_vstup-mlops-governance.md)
- [Операційна база: Термінал, Linux, Git і Docker](lectures/00_vstup-terminal-linux-git-docker.md)
- [Словник основних термінів MLOps](lectures/00_slovnyk-terminiv.md)

### Теоретичні теми (1-12)
- [Тема 1. Вступ до MLOps](lectures/topic01_vstup-do-mlops.md)
- [Тема 2. Основи Linux і Bash-скриптування](lectures/topic02_linux-bash-scripting.md)
- [Тема 3. Контейнеризація ML-моделей (Docker)](lectures/topic03_konteineryzatsiia-docker.md)
- [Тема 4. IaC для MLOps (Terraform)](lectures/topic04_iac-terraform.md)
- [Тема 5. Оркестрація в Kubernetes](lectures/topic05_kubernetes.md)
- [Тема 6. Деплой ML-сервісів у Kubernetes (EKS)](lectures/topic06_deploy-ml-kubernetes-eks.md)
- [Тема 7. GitOps через ArgoCD для Helm-деплою](lectures/topic07_argocd-helm-deploy.md)
- [Тема 8. Моніторинг та логування ML-моделей (Prometheus, Grafana, Loki)](lectures/topic08_monitoring-logging-ml.md)
- [Тема 9. Моніторинг якості моделей та відстеження експериментів (MLflow, Drift)](lectures/topic09_model-quality-drift-mlflow.md)
- [Тема 10. Автоматизоване тренування моделей (GitLab CI & AWS)](lectures/topic10_automated-training-gitlab-aws.md)
- [Тема 11. Управління моделями (Model Registry & Deployment Strategies)](lectures/topic11_model-registry-deployment-strategies.md)
- [Тема 12. Безпека ML-моделей: принципи, загрози, захист та compliance](lectures/topic12_bezpeka-ml-modeley.md)

### Практичні заняття (воркшопи з ментором)
- [Практичне заняття 2. Вибір кластерів, GPU/CPU, алерти та кейс CFO](lectures/workshop02_gpu-clusters-costs-alerts.md)
- [Практичне заняття 3. Аналіз експериментів MLflow, метрики Prometheus та training pipeline](lectures/workshop03_mlflow-prometheus-pipelines.md)

---

## Домашні завдання (управлінські артефакти)
- [ДЗ2 (Тема 5): Архітектурно-управлінський план EKS-платформи для AI/ML-продукту](homework/hw02_eks-platform-plan.md)
- [ДЗ3 (Тема 7): PM-аналіз GitOps-процесу для ML-сервісу (Argo CD)](homework/hw03_gitops-argocd-pm-analysis.md)
- [ДЗ4 (Тема 9): PM-аналіз MLflow Tracking та моніторингу в Prometheus](homework/hw04_mlflow-prometheus-pm-analysis.md)
- [ДЗ5 (Тема 10): Автоматизоване тренування моделей: контроль процесу, ризики та production-readiness](homework/ДЗ10_TrainingPipeline_Воленбовський_Геннадій.md)

---

## Фінальний проєкт: AI PM MLOps Governance Package
Індивідуальний проєкт управлінського MLOps-пакета для AI-продукту:
1. **Architectural Decision Record (ADR)**: обґрунтування ключових архітектурних рішень для стейкхолдерів.
2. **Threat model**: карта загроз для ML-системи.
3. **Release checklist**: чек-лист готовності моделі до production.
4. **Incident runbook**: план дій під час інциденту.
5. **Stakeholder presentation / summary**: презентація для нетехнічної аудиторії.
6. **Бізнес-обґрунтування MLOps-інвестиції**: TCO-розрахунок, ROI, timeline.
