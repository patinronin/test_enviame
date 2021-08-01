
 
 select employees.id as "employee_id",
 first_name, last_name,salary,  
 countries.name as "country_name",
 continents.name as "continent_name",
 continents.anual_adjustment as "anual_adjustment"
from employees 
inner join countries on countries.id = employees.country_id 
inner join continents on countries.continent_id = continents.id
where (salary < '5000');



 
 
 /*
 select employees.first_name, 
employees.last_name,
 employees.salary, 
 continents.anual_adjustment as " anual ajustment"
 from countries inner join name on  countries.id = continents.id 
 inner join employees on countries.id =  employees.country_id;
 
 

 select first_name, last_name,salary, country_id, countries.name as "nueva tabla"
from employees
inner join countries on countries.id = employees.country_id 
where (salary < '5000');
 
 
 
 
 
 */
