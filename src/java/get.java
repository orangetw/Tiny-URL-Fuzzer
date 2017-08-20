
import java.net.*;
import java.io.*;


class get{
    public static void main(String[] args) throws Exception{
        URL oracle = new URL(args[0]);
        URLConnection yc = oracle.openConnection();
        BufferedReader in = new BufferedReader(new InputStreamReader(
                                    yc.getInputStream()));
        String inputLine;
        System.out.println(in.readLine());
        in.close();
    }
}