//
//  GameViewController.swift
//  Millenial Trivia
//
//  Created by Sam Adefiyiju on 12/16/20.
//  Copyright © 2020 Sam Adefiyiju. All rights reserved.
//

import UIKit

class GameViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    
    @IBAction func startGame() {
        
        let vc = storyboard?.instantiateViewController(identifier: "game") as! Game2ViewController;
        vc.modalPresentationStyle = .fullScreen;
        present(vc, animated: true);
        
        
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
