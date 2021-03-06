El módulo contiene el desarrollo que permite diferentes tareas automáticas respecto a clientes particulares y profesionales en diferentes apartados (Presupuestos, Leads, Expediciones...)

## Parámetros de configuración
- arelux_automation_tc_part_sale_orders_qty_limit
- arelux_automation_tc_part_sale_orders_hours_since_creation
- arelux_automation_tc_part_sale_orders_user_ids
- arelux_automation_tc_part_sale_orders_team_id
- arelux_automation_tc_part_sale_orders_check_stage_id
- arelux_automation_tc_part_sale_orders_change_stage_id
- arelux_automation_tc_part_sale_orders_mail_template_id
- arelux_automation_tc_part_sale_orders_mail2_mail_template_id
- arelux_automation_tc_part_sale_orders_mail_template_id_less_15_m
- arelux_automation_tc_part_sale_orders_sms_template_id
- arelux_automation_tc_prof_so_sms_template_id_todocesped
- arelux_automation_tc_prof_so_sms_template_id_arelux
- arelux_automation_tc_prof_so_sms_template_id_both
- arelux_automation_tc_prof_so_sms_template_id_rc_todocesped
- arelux_automation_tc_prof_so_sms_template_id_rc_arelux
- arelux_automation_tc_prof_so_sms_template_id_rc_both
- arelux_automation_tc_part_repaso_mail_template_id

## Crones

### Automation Profesional Sale Orders Send SMS
Frecuencia: 1 vez cada hora

Limitaciones: Solo se envía de Lunes-Viernes en horario de 08:00 - 18:00

Descripción: Revisa todos los PV en estado "Pedido de venta" o "Bloqueado" con importe > 0€ que NO sea una reclamacion, cuyo tipo de cliente sea "profesional", con fecha de creación > '2019-06-18', que el cliente relacionado tengo un móvil definido y un país del móvil y que previamente no se le haya enviado este email y envía un SMS automático

### Automation Todocesped Particular Sale Orders 
Frecuencia: 1 vez cada hora

Limitaciones: Solo se envía de Lunes-Viernes en horario de 08:00 - 18:00 y Sábado de 09:00 - 14:00

Descripción: Revisa todos los PV en estado "Borrador" con importe > 0€ que NO sea una reclamacion, del equipo de ventas de "Online", tipo de actividad "todocesped", tipo de cliente "particular", fecha de creación > '2019-03-15' y fecha de creación < hoy -2horas con flujo de ventas asignado, flujo activo, flujo de tipo "oportunidad", probabilidad > 0, etapa del flujo "Nuevo formulario", NO asignado el flujo a ningun comercial y que el flujo sea <= 30m2. 

Le asigna un comercial al flujo, marca en el flujo que lo siguiente es una llamada al cliente (>=20 y <=30), envia un email al cliente desde el pto, envia un SMS al cliente desde el pto y le cambia la etapa al flujo

### Automation Todocesped Particular Sale Orders Mail 2
Frecuencia: 1 vez cada 2 horas

Limitaciones: Solo se envía de Lunes-Viernes en horario de 08:00 - 18:00 y Sábado de 09:00 - 14:00

Descripción: Revisa todos los PV en estado "Presupuesto enviado" que NO sean reclamacion, que tengan flujo de ventas asignado, con "fecha gestion" <= hoy -2 dias - 5minutos, flujo con probabilidad > 0 y < 100, que sea de los previamente gestionados automáticamente y a los que NO les hayamos enviado ya este email2

Envía un email automáticamente

### Automation Todocesped Particular Repaso Mail 
Frecuencia: 1 vez al día (laborable)

Descripción: Respecto a todos los flujos que están en la etapa "presupuesto enviado" se buscan si tiene algún presupuesto de importe 0€ con el transportista nacex confirmado, respecto a ese, se busca el albarán correspondiente para ver si está Hecho y si tiene expedición vinculada, si la tiene, se busca si la misma está en estado Entregado y si la fecha (date) de la expedición es <4 días de la fecha de ejecución del cron. 
En el caso de que cumpla los criterios anteriores, se busca respecto al lead inicial, si existe otro presupuesto vinculado de importe >0€ en estado 'presupuesto enviado' que NO sea una reclamación y en caso de encontrarlo, se procede a enviar un email de acuerdo a (arelux_automation_tc_part_repaso_mail_template_id) y se cambia el estado del flujo a la etapa "Repaso".
