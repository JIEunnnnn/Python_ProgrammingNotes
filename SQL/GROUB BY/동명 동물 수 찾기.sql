--이름으로 그룹화하여 조건절(having) 추가--
--WHERE절에서는 COUNT함수 사용불가!!!--


SELECT NAME, COUNT(NAME) AS COUNT
FROM ANIMAL_INS
GROUP BY NAME 
HAVING COUNT(NAME) > 1 
ORDER BY NAME ASC
