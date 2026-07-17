-- Ticket 
select * from p_express.Tabentity where ETYCODE = '';
-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>  entidad  
-- ---------------------------------------------


















-- ------------------------
-- select * from p_express.Tabentity where ETYNAME LIKE '%UDCA%';
-- select * from p_express.Tabentity where ETYCODE = '10050';
-- select * from p_express.tabsrv where etycode= '10019' and srvcode= '2020080003';
--	-------------------
-- SELECT * FROM p_express.tabtrans
-- WHERE TICKETID = ''
-- AND ETYCODE = '';
-- >> --TICKETID --SRVCODE --USERID --PAYMENTSYSTEM --TRANSVALUE --SOLICITEDATE
-- ...
-- AND SOLICITEDATE
-- BETWEEN TO_DATE ('08/06/2026', 'DD/MM/YYYY HH24:MI:SS')
-- AND TO_DATE ('09/06/2026', 'DD/MM/YYYY HH24:MI:SS');
--	-------------------
-- SELECT * FROM recaudos.tablogtx
-- WHERE TICKEDID = ''
-- AND ETYCODE = '';
-- >> LOGSTACODE --ORDID(fk) --SRVCODE --RETCODE --USERID --LOGPAYSYSTEM --TRANSVALUE --LOGSOLICITEDATE
-- ...
-- AND LOGSOLICITEDATE
-- BETWEEN TO_DATE ('08/06/2026', 'DD/MM/YYYY HH24:MI:SS')
-- AND TO_DATE ('09/06/2026', 'DD/MM/YYYY HH24:MI:SS');
--	-------------------
-- ORDER BY CREATEDATE DESC;  -- mas recietes a mas antiguas
--	-------------------
-- SELECT * FROM recaudos.tabcontrolda
-- WHERE ENROLLSEQ = ''
-- AND ETYCODE = ''
-- AND CREATEDATE
-- BETWEEN TO_DATE ('08/06/2026', 'DD/MM/YYYY HH24:MI:SS')
-- AND TO_DATE ('09/06/2026', 'DD/MM/YYYY HH24:MI:SS');
-- >> STATE --ENROLLSEQ --SRVCODE --USERID --PAYMENTSYSTEM --REFERENCE3 --PAYMENTDAY --CREATEDATE
--	-------------------
-- SELECT * FROM recaudos.tablogda ...
-- >> RETURNCODE --STATE --RETURNDESC  -SRVCODE  --ENROLLSEQ --PAYMENTTRY --TRANSVALUE
-- PAYMENTTICKET(fk-ORDID) --FILENAMEOUT--CREATEDATE --FILENAMEIN--PROCESSDATE 
--	-------------------
-- SELECT * FROM  p_express.Tabtxref ...
-- >> TICKETID -- ETYCODE
-- SELECT * FROM recaudos.taborder ...
-- >> ORDSTACODE  --ORDID   --SRVCODE --ORDDATEDUE  --ORDREFERENCE2  
--	-------------------
-- SELECT * FROM p_connector.tabtx    
-- TICKETID ETYCODE  TRAZABILITYCODE REFERENCE1 RESPONSECODE SOLICITEDATE... 

-- SELECT * FROM p_connector.tabtctx
-- TICKETID ETYCODE  TRAZABILITYCODE  REFERENCE1 RESPMESSAGE SOLICITEDATE...
--	-------------------
-- SELECT * FROM p_express.Tabcontrolag  (Notif)
-- SELECT * FROM recaudos.Tabcontrolag  (Notif)
-- >> ETYCODE --TICKETID --CTL_NOTIFY (-1 2 -7)
--	-------------------
-- validando usuario admin
-- SELECT * FROM p_express.tabadmin
-- WHERE ADMEMAIL like '% @ %';
	-- ETYCODE 10002 -- ADMEMAIL 

-- SELECT * FROM recaudos.tabper
-- WHERE PERMAIL like '% @ %';
	-- PERMAIL   -- PERPASS  --PERNAME

-- select * from p_bankagent.agentfi WHERE finame like '%DAVI%';

