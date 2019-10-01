package com.example.dell.emailverify;

import android.app.ProgressDialog;
import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.TextUtils;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;

public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    EditText mEmail,mPassword;
    Button mLogin,mRegister;
    //Firebase Variables
    FirebaseAuth mAuth;
    FirebaseAuth.AuthStateListener mAuthListner;
    FirebaseUser mUser;

    public  static final String str="Login";
    String Email,Password;

    ProgressDialog mDialog;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //Views Of Xml
        mEmail=(EditText)findViewById(R.id.login_email);
        mPassword=(EditText)findViewById(R.id.login_pass);
        mLogin=(Button)findViewById(R.id.login_Login);
        mRegister=(Button)findViewById(R.id.login_Register);
        mDialog=new ProgressDialog(this);
        //Firebase User variables
        mAuth=FirebaseAuth.getInstance();
        mUser=FirebaseAuth.getInstance().getCurrentUser();//Getting Current User
        mAuthListner=new FirebaseAuth.AuthStateListener() {
            @Override
            public void onAuthStateChanged(@NonNull FirebaseAuth firebaseAuth) {
                if(mUser!=null)
                {
                    Log.d(str,"AuthStateChange:LogOut");
                    // Disabled Auto Login Function (if signed in earlier)
                    /*Intent intent=new Intent(MainActivity.this,UserHome.class);
                    intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
                    startActivity(intent);*/
                }
                else
                {
                    Log.d(str,"AuthStateChange:LogOut");
                }
            }
        };
        //On Click Buttons
        mLogin.setOnClickListener(this);
        mRegister.setOnClickListener(this);

    }

    @Override
    protected void onStart() {
        super.onStart();
        mAuth.addAuthStateListener(mAuthListner);
    }

    @Override
    protected void onStop() {
        super.onStop();
        if(mAuthListner!=null)
        {
            mAuth.removeAuthStateListener(mAuthListner);
        }
    }

    @Override
    public void onBackPressed() {
        super.onBackPressed();
        finish();
    }

    @Override
    public void onClick(View view) {
        if(view==mLogin)
        {
            SignIn();
        }
        else if(view==mRegister)
        {
            startActivity(new Intent(MainActivity.this,Register.class));
        }
    }
    //Log In Button process
    private void SignIn() {
        Email=mEmail.getText().toString().trim();
        Password=mPassword.getText().toString().trim();
        if(TextUtils.isEmpty(Email))
        {
            Toast.makeText(MainActivity.this,"Enter Email",Toast.LENGTH_SHORT).show();
            return;
        }
        else if(TextUtils.isEmpty(Password))
        {
            Toast.makeText(MainActivity.this,"Enter Password",Toast.LENGTH_SHORT).show();
            return;
        }
        mDialog.setMessage("Logging In ....... ");
        mDialog.setIndeterminate(true);
        mDialog.show();
        mAuth.signInWithEmailAndPassword(Email,Password).addOnCompleteListener(new OnCompleteListener<AuthResult>() {
            @Override
            public void onComplete(@NonNull Task<AuthResult> task) {    //sign in with email and pass of firebase
                if(!task.isSuccessful()){
                    mDialog.dismiss();
                    Toast.makeText(MainActivity.this,"Wrong Email Id or Password",Toast.LENGTH_SHORT).show();
                }
                else {
                    mDialog.dismiss();

                    if(String.valueOf(mAuth.getCurrentUser().isEmailVerified())=="true"){       //only login if email verified
                    startActivity(new Intent(MainActivity.this,UserHome.class));}
                    else {
                        Toast.makeText(MainActivity.this," Email Not Verified !!",Toast.LENGTH_SHORT).show();
                        mAuth.signOut();
                    }
                }
            }
        });
    }
}
