package meritco;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Local {
    public static List<String> readGBK(String filePath){
    	return read(filePath, "GBK");
    }
    public static List<String> readUTF8(String filePath){
    	return read(filePath, "UTF8");
    }
    public static List<String> read(String filePath, String encoding){
    	List<String> list = new ArrayList<String>();
    	String lineTxt = null;
        try {
            File file=new File(filePath);
            if(file.isFile() && file.exists()){
                InputStreamReader read = new InputStreamReader(new FileInputStream(file),encoding);//���ǵ������ʽ
                BufferedReader bufferedReader = new BufferedReader(read);
                while((lineTxt = bufferedReader.readLine()) != null){
                	list.add(lineTxt);
                }
                read.close();
	        }
            else{
	            System.out.println("Not exist: " + filePath);
	        }
        }
        catch (Exception e) {
            System.out.println("Read file error: " + filePath);
            e.printStackTrace();
        }
        
        return list;
    }
}
