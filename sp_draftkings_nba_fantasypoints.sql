-- This stored procedure takes a table name and a minutes floor and calculates draftkings fantasy points for those players

-- Right now, assumes certain field names, is it possible to make that dynamic? 

-- Not sure it matches up to how data is stored from nba.com

-- Does not calculate bonuses for double-double and triple-double

-- Would want this calculator for other fantasy sites

DELIMITER $$

CREATE PROCEDURE `draftkings_nba_fantasy_points` (IN in_table VARCHAR(50), IN mn INT)

BEGIN

   -- dynamic query
   DECLARE from_clause VARCHAR(200);
   DECLARE where_clause VARCHAR(200);

   SET from_clause = CONCAT('FROM ', in_table);
   SET where_clause = CONCAT('WHERE MIN >= ', mn);

   -- create temporary table
   drop temporary table if exists tmp;
   SET @sql = CONCAT('create temporary table tmp engine=memory ', 
     'select `brID`, `TPM`, `TR`, `AS`, `ST`, `BK`, `PTS`,
          `TO` ', from_clause, ' ', where_clause);
   PREPARE s1 FROM @sql;
   EXECUTE s1;   

   DEALLOCATE PREPARE s1;

  -- calculate values
  SELECT brID, (prTPM + dk_fpts_TR + dk_fpts_AS + dk_fpts_ST + dk_fpts_BK + dk_fpts_PTS + dk_fpts_TO AS dk_fpts_TOT, dk_fpts_TPM, dk_fpts_TR, dk_fpts_AS, dk_fpts_ST, dk_fpts_BK, dk_fpts_PTS, dk_fpts_TO 
  FROM (
    SELECT 
      tmp.brID as brID,
      tmp.`TPM`*.5 AS dk_fpts_TPM,
      tmp.`TR`*1.25 AS dk_fpts_TR,
      tmp.`AS`*1.5 AS dk_fpts_AS,
      tmp.`ST`*2 AS dk_fpts_ST,
      tmp.`BK`*2 AS dk_fpts_BK,
      tmp.`PTS` AS dk_fpts_PTS,
      tmp.`TO`*-.5 AS dk_fpts_TO
    FROM tmp
   ) as t
   ORDER BY dk_fpts_TOT DESC;

END

DELIMITER ;
