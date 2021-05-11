// name: 字段识别
// outputs: 1
// initialize: // 部署节点后，此处添加的代码将运行一次。 \n
// finalize: // 节点正在停止或重新部署时，将运行此处添加的代码。 \n
// info: 
var getTimeStr = global.get("getTimeStr")
var data = {
    status:0,
    code:0,
	class:0,
};
var pld = msg.payload;
var s1 = pld.find(o=>o[1]=='state-1');
var s2 = pld.find(o=>o[1]=='state-2');
var s3 = pld.find(o=>o[1]=='state-3');
var s4 = pld.find(o=>o[1]=='state-4');
if(s1)data['status']=1;
if(s2)data['status']=2;
if(s3)data['status']=3;
if(s4)data['status']=4;

var c1 = pld.find(o=>o[1]=='class-1');
var c2 = pld.find(o=>o[1]=='class-2');
var c3 = pld.find(o=>o[1]=='class-3');
if(c1)data['class']=1;
if(c2)data['class']=2;
if(c3)data['class']=3;


if(data.status==0){
    msg.error = 'no status';
    return msg;
}
if(true){
	var it = pld.find(o=>o[1]=='code');
	if(!it){
		msg.error = 'no code';
		return msg;
	}
	var str = it[0];
	data['code']=str;
}
if(true){
	var it = pld.find(o=>o[1]=='num_plan');
	if(!it){
		msg.error = 'no num_plan';
		return msg;
	}
	var str = it[0];
	data['num_plan']=str;
}
if(true){
	var it = pld.find(o=>o[1]=='time_start');
	if(!it){
		msg.error = 'no time_start';
		return msg;
	}
	var str = it[0];
	if(str.length<6){
		msg.error = 'time_start length less than 6';
		return msg;
	}
	data['time_start']=getTimeStr(str);
}

if(true){
	var it2 = pld.find(o=>o[1]=='product');
	if(!it2){
		msg.error = 'no product';
		return msg;
	}
	var str2 = it2[0];
	data['product']=str2;
}
if(true){
	var it2 = pld.find(o=>o[1]=='planer');
	if(!it2){
		msg.error = 'no planer';
		return msg;
	}
	var str2 = it2[0];
	data['planer']=str2;  
}
if(true){
	var it2 = pld.find(o=>o[1]=='qc');
	if(it2){
		var str2 = it2[0];
		data['qc']=str2;  
	}
} 
if(true){
	var it2 = pld.find(o=>o[1]=='process');
	if(it2){
		var str2 = it2[0];
		data['process']=str2;  
	}
} 
if(true){
	var it2 = pld.find(o=>o[1]=='manager');
	if(it2){
		var str2 = it2[0];
		data['manager']=str2;  
	}
} 
if(true){
	var it2 = pld.find(o=>o[1]=='check');
	if(it2){
		var str2 = it2[0];
		data['check']=str2;  
	}
}
if(true){
	var it2 = pld.find(o=>o[1]=='bag');
	if(it2){
		var str2 = it2[0];
		data['bag']=str2;  
	}
}
if(true){
	var it2 = pld.find(o=>o[1]=='production');
	if(it2){
		var str2 = it2[0];
		data['production']=str2;  
	}
}
if(true){
	var it2 = pld.find(o=>o[1]=='time_done');
	if(it2){
		var str = it2[0];
		if(str.length<6){
			msg.error = 'time_done length less than 6';
			return msg;
		}
		data['time_done']=getTimeStr(str);
	}
}

if(true){
    for(var i=1;i<=12;i++){
    	var it2 = pld.find(o=>o[1]=='device--'+i);
    	if(it2){
    		var str = it2[0];
    		data['device--'+i]=str;
    	}
    	
    	var it3 = pld.find(o=>o[1]=='bad--'+i);
    	if(it3){
    		var str = it3[0];
    		data['bad--'+i]=str;
    	}  
    	
    	var it4 = pld.find(o=>o[1]=='back--'+i);
    	if(it4){
    		var str = it4[0];
    		data['back--'+i]=str;
    	} 
    	
    	var it5 = pld.find(o=>o[1]=='worker--'+i);
    	if(it5){
    		var str = it5[0];
    		data['worker--'+i]=str;
    	}  
    	
    	var it6 = pld.find(o=>o[1]=='production--'+i);
    	if(it6){
    		var str = it6[0];
    		data['production--'+i]=str;
    	}     	
    }

}


msg.db = data;
return msg;