ALTER VIEW [spends_by_country] AS
	SELECT CASE WHEN c.[country_id] = 'DE' THEN 'Exluded Country' ELSE c.[country_id] END AS [country_id], SUM([salary]) Spends 
	FROM [TRN1].[hr].[employees] a
	LEFT JOIN [hr].[departments] b 
	ON a.department_id = b.department_id
	LEFT JOIN [hr].[locations] C
	ON b.location_id = c.location_id
	GROUP BY c.country_id
 
