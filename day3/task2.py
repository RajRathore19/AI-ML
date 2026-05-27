#practice problem 2 

class Book:
    list_of_review = []
    def __init__(self,title,author):

        self.title=title
        self.author=author
    

    def newReview(self,review):
        if review == " ":
            print("empty is not a review")
        else:
            self.list_of_review.append(review)

    def count(self):
        if self.list_of_review == []:
            print("There is no review")
        else:
            count=0
            for i in self.list_of_review:
                count+=1
            print("total review is ",count)

    def display(self):
        if self.list_of_review == []:
            print("no review add review first")
        else:
         for i in self.list_of_review:
            print("Reviews are :",i);


obj=Book("Ben 10","man of action")
obj.newReview("This is good book")
obj.display()

obj.newReview("This is book")
obj.display()
obj.count()