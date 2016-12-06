package meritco;

import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
import java.util.ArrayList;
import java.util.List;

public class DecodeID {

	public static void main(String[] args) throws UnsupportedEncodingException {
		// unicode
		List<String> ls = null;
		if(args.length > 0){
			ls = Local.readGBK(args[0]);
		}
		else{
			ls = Local.readGBK("/meritco/search-mac.txt");
		}
		
//		Integer i = 0;
	//	for(String line: ls){
	//		System.out.println(++i + "|" + line + "|" + decodeId(line));
	//	}
		
		String x = "%25E2%25BC%2581%25E4%25B9%259B%25E2%25BC%2580%25E2%25BC%2583%25E2%25BC%2582%25E2%25BC%2580";
		System.out.println(x + "|" + decodeId(x));
	}

	public static String decodeId(String strId){
		if(strId == null){
			return strId;
		}
		
		// no need to decode
		if(!strId.contains("%")){
			return strId;
		}
		
		// decode many times
		String decoding0 = strId;
		String decoding1 = decode(strId);
		while(true){
			if(decoding0.equals(decoding1)){
				return decoding0;
			}
			else{
				decoding0 = decoding1;
				decoding1 = decode(decoding1);
			}
		}
		
	}
	
	private static String decode(String strId) {
		if(strId == null){
			return strId;
		}
		
		// first unicode
		if(strId.contains("%u") || strId.contains("%U")){
			return decodeUnicode(strId);
		}
		
		// second gb2312
		String strGB2312 = decodeGB2312(strId);
		
		// third utf8
		String strUTF8 = decodeUTF8(strId);
		
		// return minimum length
		return strUTF8.length() < strGB2312.length() ? strUTF8: strGB2312;
	}

	private static String decodeUTF8(String strId){
		if(strId == null){
			return strId;
		}
		
		try {
			return java.net.URLDecoder.decode(strId, "UTF8");
		} catch (Exception e) {
			return strId;
		}
	}
	
	private static String decodeGB2312(String strId){
		if(strId == null){
			return strId;
		}
		
		try {
			return java.net.URLDecoder.decode(strId, "GB2312");
		} catch (Exception e) {
			return strId;
		}
	}
	
	private static String decodeUnicode(String strId){
		List<String> lsStr = new ArrayList<String>();
		List<Boolean> lsUniCode = new ArrayList<Boolean>();

		String[] hex = strId.replace("%u", "%U").split("%U");
		if(hex.length > 0){
			lsStr.add(hex[0]);
			lsUniCode.add(false);
		}
		
		for (int i = 1; i < hex.length; i++) {
			String str = hex[i];
			if(str.length() < 4){
				lsStr.add(str);
				lsUniCode.add(false);
			}
			else if(str.length() >= 4){
				lsStr.add(str.substring(0, 4));
				lsUniCode.add(true);
				
				lsStr.add(str.substring(4, str.length()));
				lsUniCode.add(false);
			}
		}
		
		StringBuffer strUnicode = new StringBuffer();
		for(int i = 0; i < lsStr.size(); i++){
			if(lsUniCode.get(i)){
				strUnicode.append((char) Integer.parseInt(lsStr.get(i), 16));
			}
			else{
				strUnicode.append(lsStr.get(i));
			}
		}
		
		return strUnicode.toString();
	}
}
