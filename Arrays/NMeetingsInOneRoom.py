
public class Meeting{
int start, end, idx;

int getEndTime(){
return this.end;
}

int getStartTime(){
return this.start;
}

int getIdx(){
return this.idx;
}

  public Meeting(int start, int end, int idx){
    this.start = start;
    this.end = end;
     this.idx = idx;
  }
}

class Solution {

public static void sortMeetingAccordingToEndTime(Meeting[] mt){
for (int i=0;i < mt.length;i++){
for (int j=i+1;j < mt.length;j++){
if (mt[i].getEndTime() >= mt[j].getEndTime()){
Meeting temp = mt[i];
mt[i] = mt[j];
mt[j] = temp;
}
}
}
}

public static int maxMeetings(int start[], int end[], int n) {

Meeting[] mt = new Meeting[start.length];
for (int i=0;i < start.length;i++){
mt[i] = new Meeting(start[i], end[i], i+1);
}

sortMeetingAccordingToEndTime(mt);
ArrayList < Integer > res = new ArrayList <> ();

res.add(mt[0].getStartTime());
int limit = mt[0].getIdx();

for (int i=1;i < mt.length;i++){
if (mt[i].getStartTime() > limit){
res.add(mt[i].getIdx());
limit = mt[i].getStartTime();
}
}

// for (int i=0;i < res.size();i++) {System.out.print(res.get(i));}


return res.size();
}
}
