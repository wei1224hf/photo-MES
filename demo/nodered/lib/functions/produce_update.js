// name: 单据更新
// outputs: 1
// initialize: // 部署节点后，此处添加的代码将运行一次。 \n
// finalize: // 节点正在停止或重新部署时，将运行此处添加的代码。 \n
// info: 
msg.db['id'] = msg.payload[0].id;

msg.topic = "update  produce set count_updated = count_updated + 1, time_lastupdated = now() where id = '"+msg.payload[0].id+"';delete from produce_worker where  p = '"+msg.payload[0].id+"';  ";

return msg;