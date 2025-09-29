# Análisis y Segmentación de Clientes RFM

## Introducción y Objetivo de Negocio
Este proyecto aplica la metodología **RFM (Recencia, Frecuencia, Valor Monetario)** para segmentar la base de clientes. El objetivo principal es **identificar a los clientes más valiosos (Campeones) y a aquellos en riesgo de fuga** (En Riesgo) para proponer estrategias de marketing y retención altamente personalizadas y maximizar el Retorno de la Inversión (ROI).

## Resumen Ejecutivo
El análisis RFM ejecutado revela una base de clientes con alta polarización: **962 clientes se clasifican como 'Campeones'** (el 22% de la base), representando la mayor parte de nuestros ingresos y demostrando una alta lealtad. Sin embargo, se identificó que **824 clientes se encuentran 'En Riesgo'** de fuga, lo cual representa un riesgo de pérdida de valor para el negocio.

🔗 **Informe Ejecutivo Completo:** [Ver Documento PDF](https://github.com/Marcoaurelio700/proyecto1_analisis_rfm/blob/master/proyecto1_analisis_rfm/deliverables/Resumen%20Ejecutivo%20RFM.pdf)

**Recomendación de Alto Nivel:** Se debe priorizar un plan de acción dual e inmediato:
1.  **Establecer un programa de fidelización VIP** para los Campeones para defender su valor.
2.  **Lanzar una campaña de reactivación personalizada** para el segmento 'En Riesgo' para recuperar su actividad antes de que se conviertan en clientes perdidos.

## Dashboard de Power BI: Segmentación y Distribución
El dashboard interactivo fue construido en Power BI para comunicar los hallazgos de forma visual y guiar la toma de decisiones.

* **KPI Principal:** Muestra el recuento de 962 clientes en el segmento "Campeones".
* **Mapa de Calor:** Visualiza la concentración de clientes según sus puntajes de Recencia y Frecuencia, ubicando el mayor valor en la esquina superior derecha (Recencia 5, Frecuencia 5).

![Dashboard Final del Análisis RFM](https://github.com/Marcoaurelio700/proyecto1_analisis_rfm/blob/master/proyecto1_analisis_rfm/deliverables/dashboard_powerbi_rfm_final.png)

##  Conclusiones y Plan de Acción
El análisis RFM dicta dos estrategias de inversión de recursos:

| Segmento | Conclusión de Negocio | Acción Recomendada (ROI Alto) |
| :--- | :--- | :--- |
| **Campeones** | Fuente de ingresos estable. Debemos mantener su Recencia en nivel '5'. | Crear un **Programa de Fidelización VIP** (acceso anticipado, servicio prioritario). |
| **En Riesgo** | Fuga inminente. Recuperarlos es más rentable que adquirir uno nuevo. | **Campaña de Reactivación con Urgencia** (Ej. Oferta con caducidad de 48 horas). |
| **Potenciales Leales** | Alto potencial de crecimiento. | **Campañas de Up-selling** para moverlos al estatus de 'Campeones'. |

**Próximos Pasos Operacionales:**
* **Generación de Listas:** Entrega de archivos CSV con los `CustomerID` de los segmentos 'Campeones' y 'En Riesgo' al equipo de Marketing/CRM.
* **Monitoreo:** El *dashboard* será monitoreado semanalmente para evaluar el éxito de las campañas de retención.