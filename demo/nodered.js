[{"id":"392cb56b.befe8a","type":"tab","label":"流程 1","disabled":false,"info":""},{"id":"37488f19.87758","type":"MySQLdatabase","name":"","host":"127.0.0.1","port":"3306","db":"mes","tz":"","charset":"UTF8"},{"id":"9504e90f.241438","type":"exec","z":"392cb56b.befe8a","command":"python G:\\project\\photo-MES\\demo\\nodered_run.py","addpay":true,"append":"","useSpawn":"false","timer":"","oldrc":false,"name":"","x":670,"y":340,"wires":[["4d6ad74c.26fd58"],["e110cac1.7fa6d8"],["d051df19.3d37c"]]},{"id":"7b6deb8a.bf9aa4","type":"inject","z":"392cb56b.befe8a","name":"","props":[{"p":"payload"},{"p":"topic","vt":"str"}],"repeat":"","crontab":"","once":false,"onceDelay":0.1,"topic":"select remark from basic_template where code = '0505'","payload":"test.png 88,127,168,369,94,124,639,743,142,174,621,742","payloadType":"str","x":150,"y":380,"wires":[["fa0aaf48.34cc6"]]},{"id":"ca228aaf.e9aff8","type":"debug","z":"392cb56b.befe8a","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"true","targetType":"full","statusVal":"","statusType":"auto","x":980,"y":260,"wires":[]},{"id":"fa0aaf48.34cc6","type":"mysql","z":"392cb56b.befe8a","mydb":"37488f19.87758","name":"","x":250,"y":440,"wires":[["ace524f3.bb7648"]]},{"id":"ace524f3.bb7648","type":"switch","z":"392cb56b.befe8a","name":"","property":"payload.length","propertyType":"msg","rules":[{"t":"gt","v":"0","vt":"num"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":370,"y":440,"wires":[["44f58118.7c8ea"],[]]},{"id":"36b8432a.364c9c","type":"function","z":"392cb56b.befe8a","name":"","func":"var data = msg.payload[0].remark;\nvar str = data.join(',');\nstr = \"test5.png \"+str;\nmsg.payload = str;\n\nreturn msg;","outputs":1,"noerr":0,"initialize":"","finalize":"","x":710,"y":440,"wires":[["9504e90f.241438","3c672eb8.9cc2b2"]]},{"id":"44f58118.7c8ea","type":"json","z":"392cb56b.befe8a","name":"","property":"payload[0].remark","action":"","pretty":false,"x":510,"y":440,"wires":[["36b8432a.364c9c"]]},{"id":"3c672eb8.9cc2b2","type":"debug","z":"392cb56b.befe8a","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"false","statusVal":"","statusType":"auto","x":800,"y":520,"wires":[]},{"id":"e110cac1.7fa6d8","type":"debug","z":"392cb56b.befe8a","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"true","targetType":"full","statusVal":"","statusType":"auto","x":970,"y":360,"wires":[]},{"id":"d051df19.3d37c","type":"debug","z":"392cb56b.befe8a","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"true","targetType":"full","statusVal":"","statusType":"auto","x":950,"y":480,"wires":[]},{"id":"9a2598bd.d1f5f8","type":"json","z":"392cb56b.befe8a","name":"","property":"payload","action":"","pretty":false,"x":930,"y":180,"wires":[["ca228aaf.e9aff8"]]},{"id":"4d6ad74c.26fd58","type":"function","z":"392cb56b.befe8a","name":"","func":"msg.payload = msg.payload + \"YYY\";\nmsg.payload = msg.payload.replace(\",YYY\",\"]\");\nmsg.payload = msg.payload.replace(\"YYY\",\"\");\nmsg.payload = msg.payload.replace(\",XXX\",\"\");\nreturn msg;","outputs":1,"noerr":0,"initialize":"","finalize":"","x":790,"y":180,"wires":[["9a2598bd.d1f5f8","ca228aaf.e9aff8"]]},{"id":"c6b23af4.f9bba8","type":"inject","z":"392cb56b.befe8a","name":"","props":[{"p":"kill","v":"","vt":"str"}],"repeat":"","crontab":"","once":false,"onceDelay":0.1,"topic":"","x":170,"y":220,"wires":[["9504e90f.241438"]]}]