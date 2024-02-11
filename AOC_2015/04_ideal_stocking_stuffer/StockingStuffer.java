
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class StockingStuffer {

    public static void main(String[] args) {
        System.out.println(getMD5Hash("abcdef609043"));
    }

    public static String getMD5Hash(String input) {
        try {
            MessageDigest m = MessageDigest.getInstance("MD5");
            byte[] hash = m.digest("abcdef609043".getBytes());
            StringBuffer hexString = new StringBuffer();

            for (int i = 0; i < hash.length; i++) {
                if ((0xff & hash[i]) < 0x10) {
                    hexString.append("0"
                            + Integer.toHexString((0xFF & hash[i])));
                } else {
                    hexString.append(Integer.toHexString(0xFF & hash[i]));
                }
            }

            return hexString.toString();
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }

}
