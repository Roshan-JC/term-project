import com.mongodb.MongoClient;
import com.mongodb.MongoException;
import com.mongodb.WriteConcern;
import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.BasicDBObject;
import com.mongodb.DBObject;
import com.mongodb.DBCursor;
import com.mongodb.Mongo;
import com.mongodb.ServerAddress;
import java.util.Arrays;
import java.util.concurrent.CountDownLatch;
public class MongoDBJDBC {

   public static void main( String args[] ) throws InterruptedException {

	   	CountDownLatch latch = new CountDownLatch(102);
        
	   	// To connect to mongodb server
         MongoClient mongoClient = new MongoClient();         
        
         System.out.println("Stop") ;
         DB db = mongoClient.getDB( "olympics" );
         
         DBCollection coll = db.getCollection("data");
         
         DBCursor cursor = coll.find();
         int i = 1;
         
         while (cursor.hasNext()) { 
            System.out.println("selected Document: "+i); 
            System.out.println(cursor.next()); 
            i++;
         } 
         latch.await();
   }
}