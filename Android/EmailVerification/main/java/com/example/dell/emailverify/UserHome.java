package com.example.dell.emailverify;

import android.app.ProgressDialog;
import android.content.Intent;
import android.nfc.Tag;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class UserHome extends AppCompatActivity {

    FirebaseAuth mAuth;
    FirebaseUser user;
    FirebaseDatabase database;
    DatabaseReference myRef;
    TextView Name;Button Sout;
    String usname,uid;
    ProgressDialog mDialog;
    FirebaseAuth.AuthStateListener mAuthListner;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_home);
        mDialog=new ProgressDialog(this);
        mDialog.setMessage("     Loading...... ");
        mDialog.setIndeterminate(true);
        mDialog.show();
        mAuth=FirebaseAuth.getInstance();

        user=mAuth.getCurrentUser();
        database= FirebaseDatabase.getInstance();
        myRef= database.getReference("Users");
        uid=user.getUid();
        Sout=(Button)findViewById(R.id.sign_out);
        // Sign Out Button
        Sout.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                onBackPressed();
            }
        });
        // Read from the database
        if(user!=null){
        myRef.child(uid).addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                // This method is called once with the initial value and again
                // whenever data at this location is updated.
                usname = dataSnapshot.getValue(String.class);
                Name=(TextView)findViewById(R.id.user_name);
                Name.setText(usname);
                mDialog.dismiss();
            }

            @Override
            public void onCancelled(DatabaseError error) {
            }
        });}
        else{
            Toast.makeText(UserHome.this," Cant Fetch .. Contact Admin",Toast.LENGTH_SHORT).show();
            Intent intent=new Intent(UserHome.this,MainActivity.class);
            startActivity(intent);

        }



    }


    // Sign Out On Back Press
    @Override
    public void onBackPressed() {
        super.onBackPressed();
        mAuth.signOut();
        startActivity(new Intent(UserHome.this,MainActivity.class));
        Toast.makeText(UserHome.this, "Signed Out", Toast.LENGTH_SHORT).show();
        this.finish();
    }
}
