CREATE VIEW [exluded_spends_info] AS
	SELECT [first_name]
      ,[last_name]
      ,'Exluded' as [email]
      ,'Exluded' as [phone_number]
      ,'Exluded' as [hire_date]
      ,[job_id]
      ,[salary]
      ,CASE WHEN [manager_id] BETWEEN 100 AND 111 THEN 'Exluded' ELSE [manager_id] END AS [manager_id]
      ,[department_id]
  FROM [TRN1].[hr].[employees]

