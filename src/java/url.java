
import java.net.URL;
import java.net.HttpURLConnection;


class url{
    public static void main(String[] args) throws Exception{
        URL url = new URL(args[0]);
        System.out.println("scheme=" + url.getProtocol() + ", host=" + url.getHost() + ", port=" + url.getPort());
    }
}