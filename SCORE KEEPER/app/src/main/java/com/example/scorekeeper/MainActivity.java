package com.example.scorekeeper;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    int scoreA=0;
    int wicketA=0;
    double overA=0.0;

    int scoreB=0;
    int wicketB=0;
    double overB=0.0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    private void displayForTeamA(int score, int wicket) {
        TextView scoreView = (TextView) findViewById(R.id.scoreA);
        scoreView.setText(score + " / " + wicket);
    }
    private void displayOverA(double over){
        TextView overView = (TextView) findViewById(R.id.overA);
        if (over<0.6)
            overView.setText(over + " over");
        else
            overView.setText("1.0 over");
    }
    public void oneRunA(View view){
        if (overA<0.6 && wicketA<=9) {
            scoreA = scoreA + 1;
            overA = overA + 0.1;
        }
        displayOverA(overA);
        displayForTeamA(scoreA,wicketA);
    }

    public void twoRunA(View view) {
        if (overA < 0.6 && wicketA <= 9){
            scoreA = scoreA + 2;
            overA = overA + 0.1;
        }
        displayOverA(overA);
        displayForTeamA(scoreA,wicketA);
    }

    public void fourRunA(View view){
        if (overA<0.6 && wicketA<=9) {
            scoreA = scoreA + 4;
            overA = overA + 0.1;
        }
        displayOverA(overA);
        displayForTeamA(scoreA,wicketA);
    }

    public void sixRunA(View view) {
        if (overA<0.6 && wicketA<=9) {
            scoreA = scoreA + 6;
            overA = overA + 0.1;
        }
        displayOverA(overA);
        displayForTeamA(scoreA, wicketA);
    }

    public void wicketA(View view){
        if (wicketA<=9 && overA<0.6){
            overA=overA+0.1;
            wicketA=wicketA+1;
        }
        displayOverA(overA);
        displayForTeamA(scoreA,wicketA);
    }

    public void reset(View view){
        scoreA=0;
        scoreB=0;
        wicketB=0;
        wicketA=0;
        overA=0.0;
        overB=0.0;
        displayForTeamA(scoreA,wicketA);
        displayForTeamB(scoreB,wicketB);
        displayOverA(overA);
        displayOverB(overB);
    }

    private void displayForTeamB(int score, int wicket) {
        TextView scoreView = (TextView) findViewById(R.id.scoreB);
        scoreView.setText(score + " / " + wicket);
    }
    private void displayOverB(double over){
        TextView overView = (TextView) findViewById(R.id.overB);
        if (over<0.6)
            overView.setText(over + " over");
        else
            overView.setText("1.0 over");
    }
    public void oneRunB(View view){
        if (overB<0.6 && wicketB<=9) {
            scoreB = scoreB + 1;
            overB = overB + 0.1;
        }
        displayOverB(overB);
        displayForTeamB(scoreB,wicketB);
    }

    public void twoRunB(View view) {
        if (overB < 0.6 && wicketB <= 9){
            scoreB = scoreB + 2;
            overB = overB + 0.1;
        }
        displayOverB(overB);
        displayForTeamB(scoreB,wicketB);
    }

    public void fourRunB(View view){
        if (overB<0.6 && wicketB<=9) {
            scoreB = scoreB + 4;
            overB = overB + 0.1;
        }
        displayOverB(overB);
        displayForTeamB(scoreB,wicketB);
    }

    public void sixRunB(View view) {
        if (overB<0.6 && wicketB<=9) {
            scoreB = scoreB + 6;
            overB = overB + 0.1;
        }
        displayOverB(overB);
        displayForTeamB(scoreB, wicketB);
    }

    public void wicketB(View view){
        if (wicketB<=9 && overB<0.6){
            overB=overB+0.1;
            wicketB=wicketB+1;
        }
        displayOverB(overB);
        displayForTeamB(scoreB,wicketB);
    }

    public void result(View view){

        displayresult();
    }

    private void displayresult(){
        TextView resultView = (TextView) findViewById(R.id.result);

        if (overA==0.6 && overB==0.6){
            if (scoreA>scoreB)
                resultView.setText("Team A is winner");
            else if (scoreA<scoreB) {
                resultView.setText("Team B is winner");
            }
                else
                    resultView.setText("Draw");

        }
        else
            resultView.setText("IN PROGRESS");
    }
}

