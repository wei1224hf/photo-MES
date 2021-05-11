// name: 插入工序数据
// outputs: 1
// initialize: // 部署节点后，此处添加的代码将运行一次。 \n
// finalize: // 节点正在停止或重新部署时，将运行此处添加的代码。 \n
// info: 
msg.payloads.push(msg.payload);
msg.topics.push(msg.topic);
var db = msg.db;

let arr = msg.stations;
var sql_t = "";
for(var i=0;i<arr.length;i++){
	var it = arr[i];
	keys = [];
	values = [];

	keys.push("p");
	values.push("'"+db['id']+"'");
	keys.push("time_created");
	values.push("now()");	
	if(it['d']){
		keys.push("d");
		values.push("'"+it['d']+"'");
	}
	if(it['job']){
		keys.push("job");
		values.push("'"+it['job']+"'");
	}
	if(it['w']){
		keys.push("w");
		values.push("'"+it['w']+"'");
	}
	if(it['num_production']){
		keys.push("num_production");
		values.push("'"+it['num_production']+"'");
	}
	if(it['num_bad']){
		keys.push("num_bad");
		values.push("'"+it['num_bad']+"'");
	}
	if(it['num_back']){
		keys.push("num_back");
		values.push("'"+it['num_back']+"'");
	}
	
	let sql = "insert into produce_worker (";
	let sql2 = ")values(";
	sql += keys.join(",");
	sql2 += values.join(",");
	sql = sql+sql2+");";
	sql_t += sql;
}



msg.topic = sql_t;

return msg;